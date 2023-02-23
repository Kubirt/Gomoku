##
## EPITECH PROJECT, 2022
## openAI
## File description:
## Makefile
##

NAME = pbrain-gomoku-ai

MAIN = main.py

all: $(NAME)

$(NAME):
	cp $(MAIN) $(NAME)
	chmod +x $(NAME)

re: fclean all

fclean:
	$(RM) $(NAME)

.PHONY : all $(NAME) re fclean
