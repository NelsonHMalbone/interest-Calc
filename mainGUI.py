# make a gui interest calc
import PySimpleGUI as sg

# using 3 vars so the user can fill in to get
#the total of time and rate of interest

principle = 0
rate = 0
time = 0

principleInputText = sg.Text("Enter principle amount: ")
principleInput = sg.InputText()

rateInputText = sg.Text("Enter interest rate: ")
rateInput = sg.InputText()

timeInputText = sg.Text("Enter time in years: ")
timeInput = sg.InputText()

complete_button = sg.Button("Complete")

layout=[[principleInputText,principleInput],
        [rateInputText, rateInput],
        [timeInputText,timeInput]]

def main():
    # title of project
    window = sg.Window(title="Compound Interest Calculator",
                       layout= layout)
    while True:
        event, values = window.read()
        while principle <= 0:
            principleInput
            if principle <= 0:
                print("principle cant be less or equal to 0")

        while rate <= 0:
            rateInput
            if rate <= 0:
                print("Interest rate cant be less or equal to 0")

        while time <= 0:
            timeInput
            if time <= 0:
                print("Time cant be less or equal to 0")


        # end program if user closes window
        if event == "OK" or event == sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()
