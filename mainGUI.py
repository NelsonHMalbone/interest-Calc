# make a gui interest calc
import PySimpleGUI as sg

# using 3 vars so the user can fill in to get
#the total of time and rate of interest


principleInputText = sg.Text("Enter principle amount: ")
principleInput = sg.InputText()

rateInputText = sg.Text("Enter interest rate: ")
rateInput = sg.InputText()

timeInputText = sg.Text("Enter time in years: ")
timeInput = sg.InputText()

layout=[[principleInputText,principleInput],
        [rateInputText, rateInput],
        [timeInputText,timeInput]]

def main():
    # title of project
    window = sg.Window(title="Compound Interest Calculator",
                       layout= layout)
    while True:
        event, values = window.read()
        # end program if user closes window
        if event == "OK" or event == sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()
