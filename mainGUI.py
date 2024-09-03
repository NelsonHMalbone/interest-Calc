# make a gui interest calc
import PySimpleGUI as sg

def main():
    principle = 0
    rate = 0
    time = 0

    def getPrinicple(principleInput):
        while principle <= 0:
            principle = float(principleInput)
            if principle <= 0:
                print("principle cant be less or equal to 0")

    def getRate(rateInput):
        while rate <= 0:
            rate = float(rateInput)
            if rate <= 0:
                print("Interest rate cant be less or equal to 0")

    def getTime(timeInput):
        while time <= 0:
            time = int(timeInput)
            if time <= 0:
                print("Time cant be less or equal to 0")

    # using 3 vars so the user can fill in to get
    # the total of time and rate of interest

    principleInputText = sg.Text("Enter principle amount: ")
    principleInput = sg.InputText(key="principles")

    rateInputText = sg.Text("Enter interest rate: ")
    rateInput = sg.InputText(key='rates')

    timeInputText = sg.Text("Enter time in years: ")
    timeInput = sg.InputText(key='times')

    complete_button = sg.Button("Complete")
    output_label = sg.Text(key='output', text_color="green")

    layout = [[principleInputText, principleInput],
              [rateInputText, rateInput],
              [timeInputText, timeInput],
              [complete_button],
              [output_label]]

    # title of project
    window = sg.Window(title="Compound Interest Calculator",
                       layout=layout)
    while True:
        event, values = window.read()
        print(event, values)
        match event:
            case 'principles':
                principle = getPrinicple(principleInput)
            case 'rates':
                rate = getRate(rateInput)
            case 'times':
                time = getTime(timeInput)
            case 'Complete':
                total = principle * pow((1 + rate / 100), time)

                window['output'].update(value=f'Balance after {time} year/s: ${total: .2f}')
        # end program if user closes window
        if event == "OK" or event == sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()
