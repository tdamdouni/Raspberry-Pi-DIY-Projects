/** 
 * Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Amazon Software License (the "License"). You may not use this file 
 * except in compliance with the License. A copy of the License is located at
 *
 *   http://aws.amazon.com/asl/
 *
 * or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, 
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for the 
 * specific language governing permissions and limitations under the License.
 */
package com.amazon.alexa.avs.http;

import org.eclipse.jetty.client.api.ContentProvider;

import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * A {@link ContentProvider} that formats other {@link ContentProvider}s to conform to RFC 2388
 * [https://www.ietf.org/rfc/rfc2388.txt] on multipart/form-data.
 */
public class MultipartContentProvider implements ContentProvider.Typed {
    static final String BOUNDARY = "__BOUNDARY__";
    static final String NEWLINE = "\r\n";
    static final String TWO_DASHES = "--";
    static final String START_DELIMITER = NEWLINE + TWO_DASHES + BOUNDARY + NEWLINE;
    static final String END_DELIMITER = NEWLINE + TWO_DASHES + BOUNDARY + TWO_DASHES + NEWLINE;
    static final String CONTENT_TYPE = ContentTypes.MULTIPART_FORM_DATA + "; boundary=" + BOUNDARY;
    static final String PART_CONTENT_DISPOSITION_FORMAT = HttpHeaders.CONTENT_DISPOSITION
            + ": form-data; name=\"%s\"" + NEWLINE;
    static final String PART_CONTENT_TYPE_FORMAT = HttpHeaders.CONTENT_TYPE + ": %s" + NEWLINE;

    private String contentType;
    private List<PartContentProvider> parts = new ArrayList<>();

    public MultipartContentProvider() {
        this(CONTENT_TYPE);
    }

    public MultipartContentProvider(String contentType) {
        this.contentType = contentType;
    }

    public void addPart(String name, ContentProvider.Typed contentProvider) {
        addPart(name, contentProvider.getContentType(), contentProvider);
    }

    public void addPart(String name, String contentType, ContentProvider contentProvider) {
        PartContentProvider part = new PartContentProvider(contentProvider, contentType, name);
        parts.add(part);
    }

    @Override
    public long getLength() {
        long length = 0;
        for (PartContentProvider part : parts) {
            long subLength = part.getLength();
            if (subLength == -1) {
                length = -1;
                break;
            } else {
                length += subLength;
            }
        }

        if (length > -1) {
            length += END_DELIMITER.length();
        }

        return length;
    }

    @Override
    public Iterator<ByteBuffer> iterator() {
        return new MultipartIterator(parts);
    }

    @Override
    public String getContentType() {
        return contentType;
    }

    private static class PartContentProvider implements ContentProvider {
        private final ContentProvider contentProvider;
        private final String contentType;
        private final String name;
        private final String middleBoundary;

        private PartContentProvider(ContentProvider contentProvider, String contentType, String name) {
            this.contentProvider = contentProvider;
            this.contentType = contentType;
            this.name = name;
            this.middleBoundary = getMiddleBoundary();
        }

        private String getMiddleBoundary() {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.append(START_DELIMITER);
            stringBuilder.append(String.format(PART_CONTENT_DISPOSITION_FORMAT, name));
            stringBuilder.append(String.format(PART_CONTENT_TYPE_FORMAT, contentType));
            stringBuilder.append(NEWLINE);
            return stringBuilder.toString();
        }

        private Iterator<ByteBuffer> getMiddleBoundaryIterator() {
            return Stream.of(ByteBuffer.wrap(middleBoundary.getBytes())).iterator();
        }

        @Override
        public long getLength() {
            long contentLength = contentProvider.getLength();
            if (contentLength > -1) {
                return contentLength + middleBoundary.length();
            } else {
                return -1;
            }
        }

        @Override
        public Iterator<ByteBuffer> iterator() {
            List<Iterator<ByteBuffer>> iterators = Arrays.asList(getMiddleBoundaryIterator(), contentProvider.iterator());
            return new IteratorOfIterators<>(iterators);
        }
    }

    private static class MultipartIterator implements Iterator<ByteBuffer> {
        private IteratorOfIterators<ByteBuffer> iteratorOfIterators;

        private MultipartIterator(List<PartContentProvider> parts) {
            List<Iterator<ByteBuffer>> iterators = new ArrayList<>();
            if (!parts.isEmpty()) {
                iterators = parts.stream().map(Iterable::iterator).collect(Collectors.toList());
            }
            iterators.add(getEndIterator());

            iteratorOfIterators = new IteratorOfIterators<>(iterators);
        }

        private Iterator<ByteBuffer> getEndIterator() {
            return Stream.of(ByteBuffer.wrap(END_DELIMITER.getBytes())).iterator();
        }

        @Override
        public boolean hasNext() {
            return iteratorOfIterators.hasNext();
        }

        @Override
        public ByteBuffer next() {
            return iteratorOfIterators.next();
        }
    }

    private static class IteratorOfIterators<T> implements Iterator<T> {
        private final Iterator<Iterator<T>> iterators;
        private Iterator<T> currentIterator;

        private IteratorOfIterators(List<Iterator<T>> listOfIterators) {
            this.iterators = listOfIterators.iterator();
        }

        private Iterator<T> findNextIterator() {
            while (iterators.hasNext()) {
                currentIterator = iterators.next();
                if (currentIterator.hasNext()) {
                    return currentIterator;
                }
            }
            return null;
        }

        private boolean doesCurrentIteratorHaveNext() {
            return ((currentIterator != null) && currentIterator.hasNext());
        }

        @Override
        public boolean hasNext() {
            if (!doesCurrentIteratorHaveNext()) {
                currentIterator = findNextIterator();
            }

            return doesCurrentIteratorHaveNext();
        }

        @Override
        public T next() {
            return currentIterator.next();
        }
    }
}
