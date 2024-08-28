# make a gui interest calc
import PySimpleGUI as sg


def main():
    # title of project
    window = sg.Window(title="Compound Interest Calculator",
                       layout=[[]])
    while True:
        event, values = window.read()
        # end program if user closes window
        if event == "OK" or event == sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()
