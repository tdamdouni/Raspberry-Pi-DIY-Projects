//
//  main.swift
//  sroll-phat-swift
//
//  Created by Fabio Ritrovato on 27/01/2016.
//  Copyright (c) 2016 orange in a day. All rights reserved.
//

import Glibc

guard Process.arguments.count >= 2 else {
    print("\nusage: ./SimpleTextScroll \"message\" \npress CTRL-C to exit\n")
    exit(0)
}

typealias SigactionHandler = @convention(c)(Int32) -> Void

func trap(signum: Int32, action: SigactionHandler) {
    var sigAction = sigaction()
    sigAction.__sigaction_handler = unsafeBitCast(action, to: sigaction.__Unnamed_union___sigaction_handler.self)
    sigaction(signum, &sigAction, nil)
}

var pHAT: ScrollpHAT?
let handler: SigactionHandler = { signal in
    _ = try? pHAT?.clear()
    exit(0)
}
trap(signum: 2, action:handler)

do {
    pHAT = try ScrollpHAT()
    try pHAT?.setBrightness(2)
    try pHAT?.writeString(Process.arguments[1])
    while true {
        try pHAT?.scroll()
        usleep(100000)
    }
} catch let e as SMBusError {
    print(e)
}
