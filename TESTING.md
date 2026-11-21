# Generic syscall AE smoke-test package

This test branch temporarily pins Edelweiss commit
`141faf3dd59a4fdfd0a332ae7d22b2fe25c14ea9` from the draft `feature/edl-memory-backend` pull request.
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

**Caution:** No successful real-device test yet establishes that every
EX-word firmware keeps syscall 0xAE selector 3's returned scratch span
exclusive throughout EDL execution or native OS callbacks. This is
an experimental test package, not a published stable release.
