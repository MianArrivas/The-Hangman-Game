import random
from typing import List

class Data_Base_File:
	#region <Variables>
	
	__word_list : List
	__number_list : List

	#endregion

	#region <Methods>

	def get_word_list( self ) -> List:
		try:
			with open( 'data.txt', 'r', encoding='utf-8' ) as f:
				for count, word in enumerate( f ):
					self.__number_list.append( count )
					self.__word_list.append( word )
		except:
			raise FileExistsError("No fue posible abrir la base de datos, verifique que exista el archivo data.txt")

		return self.__number_list, self.__word_list		

	def pick_random_word( self ) -> str:
		return random.choice( self.__word_list )

	def add_word( self, new_word: str ) -> None:
		try:
			with open( 'data.txt', 'a', encoding='utf-8' ) as f:
				f.write( new_word )
		except:
			raise FileExistsError("Ha habido un error al agregar la palabra a la base de datos.")

	#endregion