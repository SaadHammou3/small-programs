GLOBAL _start

_start:
	mov ebx, 1 ; 
	mov ecx, 4 ; iteration counter
label:
	add ebx, ebx
	dec ecx ; decrement / inc: increment
	cmp ecx, 0 ; comparing ecx to zero to see if all iterations are complete
	jg label ; jump to label if iterations are still greater than zero
	mov eax, 1 ; sys_exit
	int 0x80 ; linux interrupt

