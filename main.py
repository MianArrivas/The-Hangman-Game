import os

from data_base_file import Data_Base_File

#region <Constants> 

DEC_VAL_ASCII_1 = 49
DEC_VAL_ASCII_2 = 50

#endregion

menu_selection : int

def print_title( ) -> None:
	print( """
		 ###   ### ######## #####    ###  #####    #####    ###### ######## #####    ###   #####
		 ###   ### ###  ### ### ###  ### ###       ### ### ### ### ###  ### ### ###  ###  #######
		 ######### ######## ###  ### ### #######   ###  #####  ### ######## ###  ### ###   #####
		 ###   ### ###  ### ###   ###### ###  ###  ###         ### ###  ### ###   ######    ###
		 ###   ### ###  ### ###    #####  ######   ###         ### ###  ### ###    #####     #
	 """  )

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

def run( ) -> None:
	
	menu( )

if __name__ == '__main__':
	run( )