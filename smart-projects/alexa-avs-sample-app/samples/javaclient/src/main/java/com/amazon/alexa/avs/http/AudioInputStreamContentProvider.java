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

import com.amazon.alexa.avs.AudioInputFormat;

import org.eclipse.jetty.client.api.ContentProvider;
import org.eclipse.jetty.client.util.InputStreamContentProvider;

import java.io.InputStream;

/**
 * A {@link ContentProvider} that streams an InputStream in chunks with size provided by
 * {@link AudioInputFormat#getChunkSizeBytes()}.
 */
public class AudioInputStreamContentProvider extends InputStreamContentProvider implements
        ContentProvider.Typed {

    public AudioInputStreamContentProvider(AudioInputFormat audioType, InputStream stream) {
        super(stream, audioType.getChunkSizeBytes());
    }

    @Override
    public String getContentType() {
        return ContentTypes.AUDIO;
    }
}
