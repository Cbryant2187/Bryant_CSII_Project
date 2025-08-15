from PyQt6.QtWidgets import *

from Main_Menu_gui import *
from Ballot_Menu_gui import *
from results_window_gui import *

class MainMenu(QMainWindow, Ui_Main_Window):
    def __init__(self) -> None:
        """
        method to create main menu with options to vote or view results
        """
        super().__init__()
        self.voting_window = None
        self.setupUi(self)
        self.voterid_list = []

        self.exit_option_button.clicked.connect(self.close)
        self.vote_option_button.clicked.connect(self.open_voting_window)

    def open_voting_window(self) -> None:
        """
        method to open voting window
        """
        self.voting_window = VotingWindow()
        self.voting_window.show()
        self.hide()


class VotingWindow(QMainWindow, Ui_input_voting_terminal):
    def __init__(self) -> None:
        """
        method to create voting/ ballet window with candidate options
        """
        super().__init__()
        self.setupUi(self)
        self.submit_button.clicked.connect(self.check_submission)
        self.custom_input.setVisible(False)
        self.radio_custom.toggled.connect(self.custom_input_box_visibility)

    def custom_input_box_visibility(self, checked: bool) -> None:
        """
        method to change input box visibility
        :param checked: boolean value representing visibility
        """
        self.custom_input.setVisible(checked)

    def check_submission(self) -> str | None:
        """
        method to check submitted ballot choice including checks for custom candidate
        :return: either nothing for errors or a string for a successful result
        """
        self.error_candidate_name_label.setText("")
        self.error_candidate_name_label.setStyleSheet("color: black;")
        voterid_text = self.voterid_input.text().strip()
        candidate = 0
        custom_candidate = 0

        if self.radio_can1.isChecked():
            candidate = 'Bianca'
        elif self.radio_can2.isChecked():
            candidate = 'Jack'
        elif self.radio_can3.isChecked():
            candidate = 'Nicole'
        elif self.radio_custom.isChecked():
            custom_candidate = self.custom_input.text()
            custom_candidate = self.validate_custom_candidate(custom_candidate)
            if custom_candidate == 0:
                self.error_candidate_name_label.setStyleSheet("color: red;")
                self.error_candidate_name_label.setText('error: enter valid name')
                return
        else:
            self.error_candidate_name_label.setStyleSheet("color: red;")
            self.error_candidate_name_label.setText('error: select candidate')
            return


        try:

            voterid_text = int(voterid_text).strip()
            if voterid_text < 10000 or voterid_text > 99999:
                self.error_candidate_name_label.setStyleSheet("color: red;")
                self.error_candidate_name_label.setText("Error: Voter ID must be 5 digits.")
                return

        except ValueError:
            self.error_candidate_name_label.setStyleSheet("color: red;")
            self.error_candidate_name_label.setText("Error: Voter ID must be a number.")
            return

        if custom_candidate == 0 and candidate != 0:
            self.error_candidate_name_label.setText(f'Voter (ID:{voterid_text}) voted for {candidate}')
            self.ballot_exit()
        elif custom_candidate == 0:
            self.error_candidate_name_label.setStyleSheet("color: red;")
            self.error_candidate_name_label.setText('error: enter valid name')
            return
        else:
            self.error_candidate_name_label.setText(f'Voter (ID:{voterid_text}) voted for {custom_candidate}')
            self.ballot_exit()

    def validate_custom_candidate(self, name: str) -> str | int:
        """
        method validating custom candidate name
        :param name: input from custom candidate input box
        :return: string of accepted name or 0 for error
        """
        try:
            str(name)
            if name.isalpha():
                name = name.strip()
                return name

            else:
                return 0

        except ValueError:
            return 0

    def ballot_exit(self) -> None:
        """
        Method to set up exit from ballot window, changing submit button to an exit button
        """
        self.submit_button.setText('Exit')
        self.submit_button.clicked.connect(self.main_return)

    def main_return(self) -> None:
        """
        method to return to main menu
        """
        self.close()
        self.main_window = MainMenu()
        self.main_window.show()






