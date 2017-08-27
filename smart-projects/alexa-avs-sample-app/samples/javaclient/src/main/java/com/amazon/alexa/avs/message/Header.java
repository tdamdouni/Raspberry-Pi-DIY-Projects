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
package com.amazon.alexa.avs.message;

public class Header {
    private String namespace;
    private String name;

    public Header() {
        // For Jackson
    }

    public Header(String namespace, String name) {
        setNamespace(namespace);
        setName(name);
    }

    public final void setNamespace(String namespace) {
        if (namespace == null) {
            throw new IllegalArgumentException("Header namespace must not be null");
        }
        this.namespace = namespace;
    }

    public final void setName(String name) {
        if (name == null) {
            throw new IllegalArgumentException("Header name must not be null");
        }
        this.name = name;
    }

    public final String getNamespace() {
        return namespace;
    }

    public final String getName() {
        return name;
    }

    @Override
    public String toString() {
        return String.format("%1$s:%2$s", namespace, name);
    }
}
