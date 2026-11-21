# Generic syscall AE smoke-test package

This test branch temporarily pins Edelweiss commit
`2006f6bb3b8dcfe2d51b9d6d7ec17186f0e539df` from the draft `feature/edl-memory-backend` pull request.
Both the embedded `example.d01` bootstrap and the `main.edl` example
are rebuilt from that same Edelweiss revision.

Download the **Example-ja** or **Example-cn** artifact from the Actions
run for this branch. Extract the ZIP, then install the complete `EXMPL`
folder using your ordinary EX-word add-in transfer process (including
`example.d01`, `main.edl`, and metadata). The `main.edl` sample
exercises standard gint display, timer, heap, trigonometry, and input.
Use EXIT to return to the shell.

Separately download **Edelweiss-ja** or **Edelweiss-cn** from the
Edelweiss feature-branch run and install its `EDELW` folder to try
`EBrew.edl` and `large-demo.edl`.

**Caution:** A8500 firmware was found actively overwriting the buffer returned by
syscall AE selector 3. The earlier test build is unsafe and has been
superseded by this safe-fallback revision. The loader uses recognized
firmware P1 arenas and caches ELF reads; real-device testing is still
required before calling this issue fixed.

**D6600 input-fix retest:** This revised loader no longer refuses all EDLs
because of stale touch-screen or keyboard state. The old `-21` launch
error came from the loader, not from any game or template code. The new
runtime only clears the event queue before and after an EDL run.
