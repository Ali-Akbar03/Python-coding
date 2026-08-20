.model small
.stack 100h

.data
    num1 DB 00110111B
    num2 DB ?

    MSG1 DB "NUM1: $"
    MSG2 DB "ENTER NUM2: $"
    MSG3 DB "SUM: $"

.code
MAIN PROC

    MOV AX, @DATA
    MOV DS, AX

    ; Show NUM1
    MOV AH, 9
    LEA DX, MSG1
    INT 21H

    MOV AH, 2
    MOV DL, num1
    INT 21H

    ; New line
    MOV AH, 2
    MOV DL, 10
    INT 21H

    MOV DL, 13
    INT 21H

    ; Enter NUM2
    MOV AH, 9
    LEA DX, MSG2
    INT 21H

    MOV AH, 1
    INT 21H
    MOV num2, AL

    ; New line
    MOV AH, 2
    MOV DL, 10
    INT 21H

    MOV DL, 13
    INT 21H

    ; Show SUM
    MOV AH, 9
    LEA DX, MSG3
    INT 21H

    MOV AL, num1
    SUB AL, 30H

    SUB num2, 30H

    ADD AL, num2
    ADD AL, 48

    ; Single character print
    MOV AH, 2
    MOV DL, AL
    INT 21H

    ; Exit
    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN