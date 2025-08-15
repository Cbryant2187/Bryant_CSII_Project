from PyQt6.QtWidgets import *

from Main_Menu_gui import *
from Ballot_Menu_gui import *
from results_window_gui import *

class MainMenu(QMainWindow, Ui_Main_Window):
    voterid_list = []

    def __init__(self):
        super().__init__()
        self.voting_window = None
        self.setupUi(self)

        self.exit_option_button.clicked.connect(self.close_window)
        self.vote_option_button.clicked.connect(self.open_voting_window)

    def close_window(self):
        self.close()

    def open_voting_window(self):
        self.voting_window = VotingWindow()
        self.voting_window.show()
        self.hide()


class VotingWindow(QMainWindow, Ui_input_voting_terminal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submit_button.clicked.connect(self.check_submission)
        self.custom_input.setVisible(False)
        self.radio_custom.toggled.connect(self.custom_input_box_visibility)

    def custom_input_box_visibility(self, checked):
        self.custom_input.setVisible(checked)

    def check_submission(self):
        self.error_candidate_name_label.setText("")
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
                self.error_candidate_name_label.setText('error: enter valid name')
                return
        else:
            self.error_candidate_name_label.setText('error: select candidate')
            return


        try:

            voterid_text = int(voterid_text)
            if voterid_text < 10000 or voterid_text > 99999:
                self.error_candidate_name_label.setText("Error: Voter ID must be 5 digits.")
                return

        except ValueError:
            self.error_candidate_name_label.setText("Error: Voter ID must be a number.")
            return

        if custom_candidate == 0:
            self.error_candidate_name_label.setText(f'Voter (ID:{voterid_text}) voted for {candidate}')
            self.ballot_exit()
        else:
            self.error_candidate_name_label.setText(f'Voter (ID:{voterid_text}) voted for {custom_candidate}')
            self.ballot_exit()

    def validate_custom_candidate(self, name: str):
        try:
            str(name)
            name = name.strip()

            return name

        except ValueError:
            return 0

    def ballot_exit(self):
        self.submit_button.setObjectName("Exit")
        self.submit_button.clicked.connect(self.main_return)

    def main_return(self):
        self.main_window = MainMenu()
        self.main_window.show()






