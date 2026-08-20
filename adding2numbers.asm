.model small
.stack 100h
.data
a db "num1 :$"
b db "Enter num2 : $"
c db "Sum: $"
num1 db 35h
num2 db ?

.code
main proc
    mov ax,@data
    mov ds,ax 
    
    
    ;num1
    lea dx,a
    mov ah,9
    int 21h
    
    mov dl,num1
    mov ah,2
    int 21h
    
    ;newline-----1
    mov ah,2
    mov dl,10
    int 21h
    mov ah,2
    mov dl,13
    int 21h
    
    ;num 2
    lea dx,b
    mov ah,9
    int 21h
    
    mov ah,1
    int 21h
    mov num2,al
    
    ;newline-----2
    mov ah,2
    mov dl,10
    int 21h
    mov ah,2
    mov dl,13
    int 21h
    
    ;sum
    lea dx,c
    mov ah,9
    int 21h
    
    ;actual
    mov al,num1
    sub al,30h
    
    sub num2,30h
    
    add al,num2
    add al,48
    
    
    ;printing
    mov ah,2
    mov dl,al
    int 21h
    
    
    
    
    ;end
    mov ah,4ch
    int 21h
    main endp
end main
   