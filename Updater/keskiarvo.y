main:
    irmovq $1, %rdi
    rrmovq %rbp, %rsi
    call summa
    halt
    
.pos 0x100
summa:
    popq %rcx
    addq %rcx, %rdx
    addq %rdi, %rbx
    subq %rsp, %rsi
    rrmovq %rbp, %rsi
    jne summa
    call jako
    ret

jako:
    addq %rdi, %rax
    subq %rbx, %rdx
    pushq %rax
    jg jako
    ret
.pos 0x300
Pino:
