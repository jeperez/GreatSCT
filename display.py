import os

class Display:
	clearSc = '';

	def __init__(self):
		if(os.name == 'nt'):
			self.clearSc = 'cls';
		else:
			self.clearSc = 'clear';

		self.clear();
		#The following is 100% functionally necessary
		print("""                     ______,------'--"-.                   
                    /                    \                 
                .--'      ,____,------.__/-._              
             ,-/         |                   \_            
          _/              \                    \           
        -'                 |                     \         
     _/                    |       __            |         
    /                    /       / ,------.   ,-----.      
   / /                  /      -' |        \-|       |     
    /                  |      '   |        | \       '     
     /                 |_____|    |        |  \      /     
    /           ,----./_______\_.  \       /   \    /      
    /          /      \           \_`-----/     \--'       
   / /        |                          / 0  0 / /        
    /\        |                                /  |        
     |         \                                  \        
      /          \                          ,---. |        
     / \_         \     \                  /    / /        
         \        |\____/                /     | |         
          \       |                     /     '  '         
            \     /                    /     /  /          
             \   /                    |      | |           
              /.-                     \______/ |           
         .__'    \                             |           
      /-`         \            \              /______      
  .--`             \            `------------/       `--.  
 /                  \                     /              \ 
___________________________________________________________
___________________________________________________________
                          ,-----.-----.                    
             ,------.----\ __   /__   /                    
            /  ,____//|  //_/  //,-----.------.            
           /  /   / /_/_/     / /  ____/_____/-----.       
--  --  --/  /___/_   \/__   /_/  /_/_ / /__   ___/-- -- --
         /  //_  _//\  \_/  //_\__   //    /  /            
_________\______/_/  \__|__/_,---/  //____/  /             
____________________________/______/______/_/              
___________________________________________________________
___________________________________________________________
Lopi                                               Dietrich""");
	

	def showOptions(self, profileDict):
		self.clear();	
		print('Please select an option');

		i = 0;
		for opt in profileDict:
			print('{0}: {1} '.format(i, opt));
			i = i+1;

	def help(self):
		self.clear();
		print("Help Menu");

	def show(self, info):
		print(info);
	
	def error(self, error):
		print(error);

	def clear(self):
		os.system(self.clearSc);
			
