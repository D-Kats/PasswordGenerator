#---DKats 2020
import PySimpleGUI as sg
import os
import itertools
import webbrowser


#---function definition
def passGenerator(Inp, Out):
	l = Inp.split(',')

	if Out == '':
		try:
			with open('wordlist.txt', 'w', encoding='utf-8') as fout:
				for i in range(2,len(l)+1):					
					wordlist = list(itertools.permutations(l,i))
					for current_pass in range(len(wordlist)):
						str_pass = ''
						fout.write(f'{str_pass.join([str(password) for password in wordlist[current_pass]])}\n')						
				sg.PopupOK(f'Wordlist text file created succesfully in {os.getcwd()} folder', title=':)')
		except Exception as e:
			sg.PopupOK(f'Error: {e}. Please check output folder write permissions', title='!')
	else:
		try:			
			with open(f'{Out}\\wordlist.txt', 'w', encoding='utf-8') as fout:
				for i in range(2,len(l)+1):					
					wordlist = list(itertools.permutations(l,i))
					for current_pass in range(len(wordlist)):
						str_pass = ''
						fout.write(f'{str_pass.join([str(password) for password in wordlist[current_pass]])}\n')					
				sg.PopupOK(f'Wordlist text file created succesfully in {Out} folder', title=':)')
		except Exception as e:
			sg.PopupOK(f'Error: {e}. Please check output folder write permissions', title='!')


#---menu definition
menu_def = [['File', ['Exit']],
			['Help', ['Documentation', 'About']],] 

#Frames Layout
ButtonsFrameLayout = [[sg.Button('Exit', size=(7,1)), sg.Button('Run', size=(7,1))]]

InputFrameLayout = [[sg.Text('Provide the characters for the wordlist\n(separate characters by using a coma)')],
					[sg.Input(key='-CHARS-')]]

OutputFrameLayout = [[sg.Text('Give an output folder for the text file\n(Default location is the exe folder)')],
					[sg.Input(key='-OUT-', readonly=True), sg.FolderBrowse()]]

#---GUI definition
layout = [[sg.Menu(menu_def, key='-MENUBAR-')],
			[sg.Frame('INPUT',InputFrameLayout, element_justification='c')],
			[sg.Frame('OUTPUT',OutputFrameLayout, element_justification='c')],
			[sg.Frame('',ButtonsFrameLayout, element_justification='c')],
			# [sg.ProgressBar(100, key='-PROGRESSBAR-', orientation='horizontal', style='vista')],
			[sg.StatusBar('\nPassword Generator Ver. 1.0.0', relief='flat', justification='r', text_color='#435c69')]]

window = sg.Window('PasswordGenerator', layout, element_justification='c') 

#---run
while True:
	event, values = window.read()
	# print(event, values)
	if event in (sg.WIN_CLOSED, 'Exit'):
		break

	#---menu events
	if event == 'Documentation':
		try:
			webbrowser.open_new('https://github.com/D-Kats/PasswordGenerator/blob/main/README.md')
		except:
			sg.PopupOK('Visit https://github.com/D-Kats for documentation', title='Documentation')
	if event == 'About':
		sg.PopupOK('PasswordGenerator Ver. 1.0.0 \n\n --DKats 2020', title='-About-', background_color='#2a363b')

	if event == 'Run':
		if values['-CHARS-'] == '':
			sg.PopupOK('Please give characters for the wordlist', title='!')
		elif ',' not in values['-CHARS-']:
			sg.PopupOK('Please give more than one character for the wordlist. Separate them by coma!', title='!')
		else:
			passGenerator(values['-CHARS-'], values['-OUT-'])


window.close()
