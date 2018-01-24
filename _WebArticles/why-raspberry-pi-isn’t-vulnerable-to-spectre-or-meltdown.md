# Why Raspberry Pi isn’t vulnerable to Spectre or Meltdown

_Captured: 2018-01-13 at 22:02 from [www.raspberrypi.org](https://www.raspberrypi.org/blog/why-raspberry-pi-isnt-vulnerable-to-spectre-or-meltdown/?utm_source=Hackster.io+newsletter&utm_campaign=7344840f43-EMAIL_CAMPAIGN_2017_07_26&utm_medium=email&utm_term=0_6ff81e3e5b-7344840f43-141949901&mc_cid=7344840f43&mc_eid=1c68da4188)_

Over the last couple of days, there has been a lot of discussion about a pair of security vulnerabilities nicknamed [Spectre and Meltdown](https://spectreattack.com/). These affect all modern Intel processors, and (in the case of Spectre) many AMD processors and [ARM cores](https://developer.arm.com/support/security-update). Spectre allows an attacker to bypass software checks to read data from arbitrary locations in the current address space; Meltdown allows an attacker to read data from arbitrary locations in the operating system kernel's address space (which should normally be inaccessible to user programs).

Both vulnerabilities exploit performance features (_caching_ and _speculative execution_) common to many modern processors to leak data via a so-called side-channel attack. Happily, the Raspberry Pi isn't susceptible to these vulnerabilities, because of the particular ARM cores that we use.

To help us understand why, here's a little primer on some concepts in modern processor design. We'll illustrate these concepts using simple programs in Python syntax like this one:
    
    
    t = a+b
    u = c+d
    v = e+f
    w = v+g
    x = h+i
    y = j+k
    

While the processor in your computer doesn't execute Python directly, the statements here are simple enough that they roughly correspond to a single machine instruction. We're going to gloss over some details (notably [pipelining](https://en.wikipedia.org/wiki/Pipeline_\(computing\)) and [register renaming](https://en.wikipedia.org/wiki/Register_renaming)) which are very important to processor designers, but which aren't necessary to understand how Spectre and Meltdown work.

For a comprehensive description of processor design, and other aspects of modern computer architecture, you can't do better than Hennessy and Patterson's classic _[Computer Architecture: A Quantitative Approach](https://www.amazon.co.uk/Computer-Architecture-Quantitative-Approach-Kaufmann/dp/012383872X)_.

## What is a scalar processor?

The simplest sort of modern processor executes one instruction per cycle; we call this a scalar processor. Our example above will execute in six cycles on a scalar processor.

Examples of scalar processors include the Intel 486 and the ARM1176 core used in Raspberry Pi 1 and Raspberry Pi Zero.

## What is a superscalar processor?

The obvious way to make a scalar processor (or indeed any processor) run faster is to increase its clock speed. However, we soon reach limits of how fast the logic gates inside the processor can be made to run; processor designers therefore began to look for ways to do several things at once.

An in-order superscalar processor examines the incoming stream of instructions and tries to execute more than one at once, in one of several _pipelines_ (_pipes_ for short), subject to dependencies between the instructions. Dependencies are important: you might think that a two-way superscalar processor could just pair up (or _dual-issue_) the six instructions in our example like this:
    
    
    t, u = a+b, c+d
    v, w = e+f, v+g
    x, y = h+i, j+k
    

But this doesn't make sense: we have to compute `v` before we can compute `w`, so the third and fourth instructions can't be executed at the same time. Our two-way superscalar processor won't actually be able to find anything to pair with the third instruction, so our example will execute in four cycles:
    
    
    t, u = a+b, c+d
    v    = e+f                   # second pipe does nothing here
    w, x = v+g, h+i
    y    = j+k
    

Examples of superscalar processors include the Intel Pentium, and the ARM Cortex-A7 and Cortex-A53 cores used in Raspberry Pi 2 and Raspberry Pi 3 respectively. Raspberry Pi 3 has only a 33% higher clock speed than Raspberry Pi 2, but has roughly double the performance: the extra performance is partly a result of Cortex-A53's ability to dual-issue a broader range of instructions than Cortex-A7.

## What is an out-of-order processor?

Going back to our example, we can see that, although we have a dependency between `v` and `w`, we have other independent instructions later in the program that we could potentially have used to fill the empty pipe during the second cycle. An out-of-order superscalar processor has the ability to shuffle the order of incoming instructions (again subject to dependencies) in order to keep its pipes busy.

An out-of-order processor might effectively swap the definitions of `w` and `x` in our example like this:
    
    
    t = a+b
    u = c+d
    v = e+f
    x = h+i
    w = v+g
    y = j+k
    

allowing it to execute in three cycles:
    
    
    t, u = a+b, c+d
    v, x = e+f, h+i
    w, y = v+g, j+k
    

Examples of out-of-order processors include the Intel Pentium 2 (and most subsequent Intel and AMD x86 processors with the exception of some Atom and Quark devices), and many recent ARM cores, including Cortex-A9, -A15, -A17, and -A57.

## What is branch prediction?

Our example above is a straight-line piece of code. Real programs aren't like this of course: they also contain both forward branches (used to implement conditional operations like `if` statements), and backward branches (used to implement loops). A branch may be unconditional (always taken), or conditional (taken or not, depending on a computed value); it may be _direct_ (explicitly specifying a target address) or _indirect_ (taking its target address from a register, memory location or the processor stack).

While fetching instructions, a processor may encounter a conditional branch which depends on a value which has yet to be computed. To avoid a stall, it must guess which instruction to fetch next: the next one in memory order (corresponding to an untaken branch), or the one at the branch target (corresponding to a taken branch). A _branch predictor_ helps the processor make an intelligent guess about whether a branch will be taken or not. It does this by gathering statistics about how often particular branches have been taken in the past.

Modern branch predictors are extremely sophisticated, and can generate very accurate predictions. Raspberry Pi 3's extra performance is partly a result of improvements in branch prediction between Cortex-A7 and Cortex-A53. However, by executing a crafted series of branches, an attacker can mis-train a branch predictor to make poor predictions.

## What is speculation?

Reordering sequential instructions is a powerful way to recover more instruction-level parallelism, but as processors become wider (able to triple- or quadruple-issue instructions) it becomes harder to keep all those pipes busy. Modern processors have therefore grown the ability to _speculate_. Speculative execution lets us issue instructions which might turn out not to be required (because they may be branched over): this keeps a pipe busy (use it or lose it!), and if it turns out that the instruction isn't executed, we can just throw the result away.

Speculatively executing unnecessary instructions (and the infrastructure required to support speculation and reordering) consumes extra energy, but in many cases this is considered a worthwhile trade-off to obtain extra single-threaded performance. The branch predictor is used to choose the most likely path through the program, maximising the chance that the speculation will pay off.

To demonstrate the benefits of speculation, let's look at another example:
    
    
    t = a+b
    u = t+c
    v = u+d
    if v:
       w = e+f
       x = w+g
       y = x+h
    

Now we have dependencies from `t` to `u` to `v`, and from `w` to `x` to `y`, so a two-way out-of-order processor without speculation won't ever be able to fill its second pipe. It spends three cycles computing `t`, `u`, and `v`, after which it knows whether the body of the `if` statement will execute, in which case it then spends three cycles computing `w`, `x`, and `y`. Assuming the `if` (implemented by a branch instruction) takes one cycle, our example takes either four cycles (if `v` turns out to be zero) or seven cycles (if `v` is non-zero).

If the branch predictor indicates that the body of the `if` statement is likely to execute, speculation effectively shuffles the program like this:
    
    
    t = a+b
    u = t+c
    v = u+d
    w_ = e+f
    x_ = w_+g
    y_ = x_+h
    if v:
       w, x, y = w_, x_, y_
    

So we now have additional instruction level parallelism to keep our pipes busy:
    
    
    t, w_ = a+b, e+f
    u, x_ = t+c, w_+g
    v, y_ = u+d, x_+h
    if v:
       w, x, y = w_, x_, y_
    

Cycle counting becomes less well defined in speculative out-of-order processors, but the branch and conditional update of `w`, `x`, and `y` are (approximately) free, so our example executes in (approximately) three cycles.

## What is a cache?

In the good old days*, the speed of processors was well matched with the speed of memory access. My BBC Micro, with its 2MHz 6502, could execute an instruction roughly every 2µs (microseconds), and had a memory cycle time of 0.25µs. Over the ensuing 35 years, processors have become very much faster, but memory only modestly so: a single Cortex-A53 in a Raspberry Pi 3 can execute an instruction roughly every 0.5ns (nanoseconds), but can take up to 100ns to access main memory.

At first glance, this sounds like a disaster: every time we access memory, we'll end up waiting for 100ns to get the result back. In this case, this example:
    
    
    a = mem[0]
    b = mem[1]
    

would take 200ns.

However, in practice, programs tend to access memory in relatively predictable ways, exhibiting both temporal locality (if I access a location, I'm likely to access it again soon) and spatial locality (if I access a location, I'm likely to access a nearby location soon). Caching takes advantage of these properties to reduce the average cost of access to memory.

A cache is a small on-chip memory, close to the processor, which stores copies of the contents of recently used locations (and their neighbours), so that they are quickly available on subsequent accesses. With caching, the example above will execute in a little over 100ns:
    
    
    a = mem[0]    # 100ns delay, copies mem[0:15] into cache
    b = mem[1]    # mem[1] is in the cache
    

From the point of view of Spectre and Meltdown, the important point is that if you can time how long a memory access takes, you can determine whether the address you accessed was in the cache (short time) or not (long time).

## What is a side channel?

From Wikipedia:

"… a side-channel attack is any attack based on information gained from the physical implementation of a cryptosystem, rather than brute force or theoretical weaknesses in the algorithms (compare cryptanalysis). For example, timing information, power consumption, electromagnetic leaks or even sound can provide an extra source of information, which can be exploited to break the system."

Spectre and Meltdown are side-channel attacks which deduce the contents of a memory location which should not normally be accessible by using timing to observe whether another, accessible, location is present in the cache.

## Putting it all together

Now let's look at how speculation and caching combine to permit a Meltdown-like attack on our processor. Consider the following example, which is a user program that sometimes reads from an illegal (kernel) address, resulting in a fault (crash):
    
    
    t = a+b
    u = t+c
    v = u+d
    if v:
       w = kern_mem[address]   # if we get here, fault
       x = w&0x100
       y = user_mem[x]
    

Now, provided we can train the branch predictor to believe that `v` is likely to be non-zero, our out-of-order two-way superscalar processor shuffles the program like this:
    
    
    t, w_ = a+b, kern_mem[address]
    u, x_ = t+c, w_&0x100
    v, y_ = u+d, user_mem[x_]
    
    if v:
       # fault
       w, x, y = w_, x_, y_      # we never get here
    

Even though the processor always speculatively reads from the kernel address, it must defer the resulting fault until it knows that `v` was non-zero. On the face of it, this feels safe because either:

  * `v` is zero, so the result of the illegal read isn't committed to `w`
  * `v` is non-zero, but the fault occurs before the read is committed to `w`

However, suppose we flush our cache before executing the code, and arrange `a`, `b`, `c`, and `d` so that `v` is actually zero. Now, the speculative read in the third cycle:
    
    
    v, y_ = u+d, user_mem[x_]
    

will access either userland address `0x000` or address `0x100` depending on the eighth bit of the result of the illegal read, loading that address and its neighbours into the cache. Because `v` is zero, the results of the speculative instructions will be discarded, and execution will continue. If we time a subsequent access to one of those addresses, we can determine which address is in the cache. Congratulations: you've just read a single bit from the kernel's address space!

The real Meltdown exploit is substantially more complex than this (notably, to avoid having to mis-train the branch predictor, the authors prefer to execute the illegal read unconditionally and handle the resulting exception), but the principle is the same. Spectre uses a similar approach to subvert software array bounds checks.

## Conclusion

Modern processors go to great lengths to preserve the abstraction that they are in-order scalar machines that access memory directly, while in fact using a host of techniques including caching, instruction reordering, and speculation to deliver much higher performance than a simple processor could hope to achieve. Meltdown and Spectre are examples of what happens when we reason about security in the context of that abstraction, and then encounter minor discrepancies between the abstraction and reality.

The lack of speculation in the ARM1176, Cortex-A7, and Cortex-A53 cores used in Raspberry Pi render us immune to attacks of the sort.

* days may not be that old, or that good
