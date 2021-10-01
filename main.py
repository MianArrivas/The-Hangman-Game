import os
import time

from data_base_file import Data_Base_File

#region <Constants> 

DEC_VAL_ASCII_1 = 49
DEC_VAL_ASCII_2 = 50

PLAY = 1
ADD_WORD = 2
DELAY_CLEARING_TIME = 3

NOT_ALLOWED_CHARACTERS = "¡!#$[]%&/()=¿?0123456789.:+-_*|°¬,;´¨\\<>^ \t" 

#endregion

#region <Variables>

menu_selection : int
attempt: int

#endregion

def print_title( ) -> None:
	print( """
		###   ### ######## #####    ###  #####    #####    ###### ######## #####    ###   #####
		###   ### ###  ### ### ###  ### ###       ### ### ### ### ###  ### ### ###  ###  #######
		######### ######## ###  ### ### #######   ###  #####  ### ######## ###  ### ###   #####
		###   ### ###  ### ###   ###### ###  ###  ###         ### ###  ### ###   ######    ###
		###   ### ###  ### ###    #####  ######   ###         ### ###  ### ###    #####     #
	 """  )

def draw_hangman( attempts: int ) -> None:
	if attempts == 1:
		print("""
		   	#############
		   	###         #
		   	###
		   	###
		   	###
		   	###
		   	###
		   	###
		   	###
		   	###
		   	###
		    ###
		###########	
		""")
	if attempts == 2:
		print("""
		   	#############
		   	###         #
		   	###        ###
		   	###       #   #
		   	###        ###
		   	###
		   	###
		   	###
		   	###
		   	###
		   	###
		   	###
		###########	
		""")
	if attempts == 3:
		print("""
		   	#############
		   	###         #
		   	###        ###
		   	###       #   #
		   	###        ###
		   	###         #
		   	###         #
		   	###         #
		   	###         #
		   	###
		   	###
		   	###
		###########	
		""")
	if attempts == 4:
		print("""
		   	#############
		   	###         #
		   	###        ###
		   	###       #   #
		   	###    #   ###
		   	###     ##  #
		   	###       ###
		   	###         #
		   	###         #
		   	###
		   	###
		   	###
		###########	
		""")
	if attempts == 5:
		print("""
		   	#############
		   	###         #
		   	###        ###
		   	###       #   #
		   	###    #   ###   #
		   	###     ##  #  ##
		   	###       #####
		   	###         #
		   	###         #
		   	###
		   	###
		   	###
		###########	
		""")
	if attempts == 6:
		print("""
		   	#############
		   	###         #
		   	###        ###
		   	###       #   #
		   	###    #   ###   #
		   	###     ##  #  ##
		   	###       #####
		   	###         #
		   	###         #
		   	###        #
		   	###       #
		   	###
		###########	
		""")
	if attempts == 7:
		print("""
		   	#############
		   	###         #
		   	###        ###
		   	###       #   #
		   	###    #   ###   #
		   	###     ##  #  ##
		   	###       #####
		   	###         #
		   	###         #
		   	###        # #
		   	###       #   #
		   	###
		###########	
		""")

def print_loser( ) -> None:
	print("""
	   	###       ######    ###### ######## ########    #####   #####   ##### 
	   	###      ###  ### ###      ###      ###   ###  ####### ####### #######
	   	###      ###  ###  ######  ######   #######     #####   #####   ##### 
	   	###      ###  ###      ### ###      ###  ###     ###     ###     ###  
	   	########  ######  #######  ######## ###   ###     #       #       #   
	""")

def print_winner( ) -> None:
	print("""
	   	###         ###  #######  #####    ###  #####    ###  ########  ########    #####   #####   ##### 
	   	###         ###    ###    ### ###  ###  ### ###  ###  ###       ###   ###  ####### ####### #######
	   	###  ####   ###    ###    ###  ### ###  ###  ### ###  ######    #######     #####   #####   ##### 
	   	### ### ### ###    ###    ###   ######  ###   ######  ###       ###  ###     ###     ###     ###  
	   	######   ######  #######  ###    #####  ###    #####  ########  ###   ###     #       #       #   
	""")

def clear_screen ( ) -> None:
	os.system( "cls" )

def menu ( ) -> int:
	print_title()

	right_input = False
	
	while not right_input:
		menu_selection = input( "\n\t1 - Jugar\n\t2 - Agregar palabra\nSeleccion: ")
		if ord( menu_selection[0] ) == DEC_VAL_ASCII_1 or ord( menu_selection[0] ) == DEC_VAL_ASCII_2:
			menu_selection = int( menu_selection )
			break

		clear_screen( )
		print_title( )

	return menu_selection

def add_word_to_db( new_word: str ) -> None:	
	for char in new_word:
		if char in NOT_ALLOWED_CHARACTERS:
			raise ValueError(f"Se ha ingresado una palabra con caracteres no validos.\nLos siguientes caracteres no son válidos: \" {NOT_ALLOWED_CHARACTERS} \"")

	db = Data_Base_File()
	db.add_word(new_word)

def uncover_underscore( underscore_string: str, position_to_uncover: int, guessed_letter: str) -> str:
	# Convert the string into a List type so I can replace the the proper underscore
	temp_str = list( underscore_string )

	# Due to the underscore string I use uses the following format "_ _ _" (Underscore-space)
	# I generate the right position to replace for a letter
	position_to_uncover = 2 * position_to_uncover

	temp_str[position_to_uncover] = guessed_letter

	underscore_string = "".join(temp_str)

	return underscore_string

def game( ) -> None:
	attempt = 0
	used_letters = []

	db = Data_Base_File( )
	word_to_guess = db.pick_random_word( ).replace('\n', '')
	word_size = len( word_to_guess )

	letters_to_win = word_size
	
	word_size_underscores = "_ "
	for letter in range(word_size - 1):
		word_size_underscores += "_ "

	game_over = False
	while not game_over:
		#TODO: Crear el juego, pedir al usuario una letra, si la letra coincide con una de la palabra, agregar la letra a los dashes, de lo contrario, comienza a imprimir al ahorcado
		clear_screen( )
		print_title( )

		print( f"\n\t\t> Letras faltantes para ganar: - {letters_to_win} - <\n" )

		draw_hangman( attempt )

		print( f"\n\t\t Palabra: {word_size_underscores}" )
		
		print(f"\n> Letras usadas: {used_letters} <")

		if( attempt >= 7 ):
			game_over = True
			continue

		if( letters_to_win <= 0):
			break

		letter = input( "\n\n\t Adivina una letra: " )

		used_letters.append(f"{letter} - ")

		letter_position = word_to_guess.find(letter)
		if(letter_position != -1):
			letters_to_win -= 1

			word_size_underscores = uncover_underscore(word_size_underscores, letter_position, letter)
			continue

		attempt += 1
	
	print( f"\n\t\tLa palabra era: - {word_to_guess} - " )

	if game_over:
		print_loser()
	else:
		print_winner( )

	time.sleep(3.5)

	clear_screen( )
	print_title( )

def run( ) -> None:
	clear_screen( )
	
	menu_selection = menu( )
	
	if menu_selection == PLAY:
		game( )
	
	if menu_selection == ADD_WORD:
		done = False

		while not done:
			word = input( "Introduzca una nueva palabra: " )
			try:
				add_word_to_db( word )

				print( f"La palabra \'{word}\' ha sido añadida a la base de datos.")

				done = True

			except ValueError as ex:
				print( ex )

			except Exception as ex:
				print( ex )

			finally:
				time.sleep( DELAY_CLEARING_TIME )

				clear_screen( )
				print_title( )



if __name__ == '__main__':
	while True:
		run( )