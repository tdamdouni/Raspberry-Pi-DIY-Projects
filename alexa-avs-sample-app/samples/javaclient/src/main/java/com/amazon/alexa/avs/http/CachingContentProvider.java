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
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.nio.ByteBuffer;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

/**
 * Decorates a {@link ContentProvider} and adds caching behavior to allow for HTTP request retries.
 */
public class CachingContentProvider implements ContentProvider.Typed {

    private static final Logger log = LoggerFactory.getLogger(CachingContentProvider.class);

    private ContentProvider contentProvider;
    private CachingIterator cachingIterator;

    public CachingContentProvider(ContentProvider contentProvider) {
        this.contentProvider = contentProvider;
    }

    @Override
    public long getLength() {
        return contentProvider.getLength();
    }

    @Override
    public Iterator<ByteBuffer> iterator() {

        if (cachingIterator == null) {
            log.info("Create new CachingIterator");
            cachingIterator = new CachingIterator(contentProvider.iterator());
            return cachingIterator;
        } else {
            log.info("Using cached iterator");
            return cachingIterator.getCachedIterator();
        }
    }

    @Override
    public String getContentType() {
        if (contentProvider instanceof ContentProvider.Typed) {
            return ((ContentProvider.Typed) contentProvider).getContentType();
        }
        return null;
    }

    /**
     * Keeps a cache of ByteBuffers that come from the original iterator.
     */
    public static class CachingIterator implements Iterator<ByteBuffer> {
        private Iterator<ByteBuffer> originalIterator;
        private boolean cacheBytes = true;
        private List<ByteBuffer> cache = new LinkedList<ByteBuffer>();

        public CachingIterator(Iterator<ByteBuffer> originalIterator) {
            this.originalIterator = originalIterator;
        }

        public Iterator<ByteBuffer> getCachedIterator() {
            cacheBytes = false;
            return cache.iterator();
        }

        @Override
        public boolean hasNext() {
            return originalIterator.hasNext();
        }

        @Override
        public ByteBuffer next() {
            ByteBuffer byteBuffer = originalIterator.next();
            if (cacheBytes) {
                cache.add(byteBuffer.duplicate());
            } else {
                log.warn("next was called on iterator after the cached bytes were returned");
            }
            return byteBuffer;
        }
    }
}
