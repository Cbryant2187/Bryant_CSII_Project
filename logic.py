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
        self.can1_total = 0
        self.can2_total = 0
        self.can3_total = 0
        self.custom_can_total = 0

        self.exit_option_button.clicked.connect(self.open_results_window)
        self.vote_option_button.clicked.connect(self.open_voting_window)

    def open_voting_window(self) -> None:
        """
        method to open voting window
        """
        self.voting_window = VotingWindow(self)
        self.voting_window.show()
        self.hide()


    def open_results_window(self) -> None:
        """
        method to open results window
        """
        self.results_window = ResultsWindow(self)
        self.results_window.show()
        self.hide()


class VotingWindow(QMainWindow, Ui_input_voting_terminal):
    def __init__(self, main_menu) -> None:
        """
        method to create voting/ ballet window with candidate options
        :param main_menu: keeps status of main menu variables
        """
        super().__init__()
        self.main_menu = main_menu
        self.setupUi(self)
        self.submit_button.clicked.connect(self.check_submission)
        self.custom_input.setVisible(False)
        self.radio_custom.toggled.connect(self.custom_input_box_visibility)

    def custom_input_box_visibility(self, status: bool) -> None:
        """
        method to change input box visibility
        :param status: boolean value representing visibility
        """
        self.custom_input.setVisible(status)

    def check_submission(self) -> str | None:
        """
        method to check submitted ballot choice including checks for custom candidate
        :return: either nothing for errors or a string for a successful result
        """
        self.error_candidate_name_label.setText("")
        self.error_candidate_name_label.setStyleSheet("color: black;")
        voterid_text = self.voterid_input.text().strip()
        candidate = None
        custom_candidate = None

        if self.radio_can1.isChecked():
            candidate = 'Bianca'
        elif self.radio_can2.isChecked():
            candidate = 'Jack'
        elif self.radio_can3.isChecked():
            candidate = 'Nicole'
        elif self.radio_custom.isChecked():
            custom_candidate = self.custom_input.text()
            custom_candidate = self.validate_custom_candidate(custom_candidate)
            if custom_candidate is None:
                self.error_candidate_name_label.setStyleSheet("color: red;")
                self.error_candidate_name_label.setText('error: enter valid name')
                return
        else:
            self.error_candidate_name_label.setStyleSheet("color: red;")
            self.error_candidate_name_label.setText('error: select candidate')
            return


        try:

            voterid_text = voterid_text.strip()
            voterid_num = int(voterid_text)
            if voterid_num < 10000 or voterid_num > 99999:
                self.error_candidate_name_label.setStyleSheet("color: red;")
                self.error_candidate_name_label.setText("Error: Voter ID must be 5 digits.")
                return

            if voterid_num in self.main_menu.voterid_list:
                self.error_candidate_name_label.setStyleSheet("color: red;")
                self.error_candidate_name_label.setText("Error: Voter ID has already voted.")
                return

        except ValueError:
            self.error_candidate_name_label.setStyleSheet("color: red;")
            self.error_candidate_name_label.setText("Error: Voter ID must be a number.")
            return

        if custom_candidate is None and candidate is not None:
            self.error_candidate_name_label.setText(f'Voter (ID:{voterid_text}) voted for {candidate}')
            self.main_menu.voterid_list.append(voterid_num)
            self.ballot_exit()
        elif custom_candidate is None:
            self.error_candidate_name_label.setStyleSheet("color: red;")
            self.error_candidate_name_label.setText('error: enter valid name')
            return
        else:
            self.error_candidate_name_label.setText(f'Voter (ID:{voterid_text}) voted for {custom_candidate}')
            self.main_menu.voterid_list.append(voterid_num)
            self.ballot_exit()

    def validate_custom_candidate(self, name: str) -> str | None:
        """
        method validating custom candidate name
        :param name: input from custom candidate input box
        :return: string of accepted name or None for error
        """
        try:
            str(name)
            if name.isalpha():
                name = name.strip()
                return name

            else:
                return None

        except ValueError:
            return None

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
        self.main_menu.show()


class ResultsWindow(QMainWindow, Ui_results_window):
    def __init__(self, main_menu) -> None:
        """
        method to create results window
        :param main_menu: preserves main menu to keep status of voterid and count lists
        """
        super().__init__()
        self.main_menu = main_menu
        self.setupUi(self)
        self.results_exit_button.clicked.connect(self.close)
        
        self.can1_total = main_menu.can1_total
        self.can2_total = main_menu.can2_total
        self.can3_total = main_menu.can3_total
        self.custom_can_total = main_menu.custom_can_total

        #vote_percent1 = self.can1_total / (self.can2_total + self.can3_total + self.custum_can_total)
        #vote_percent2 = self.can2_total / (self.can3_total + self.can1_total + custum_can_total)
        #vote_percent3 = self.can3_total / (self.can1_total + self.can2_total + custum_can_total)
        #custom_can_percent = self.custom_can_total / (self.can1_total + self.can2_total + self.can3_total)


        #self.can1_result.setText(f"Bianca received {self.can1_total} : {vote_percent1}")
        #self.can2_result.setText(f"Jack received {self.can1_total} : {vote_percent2}")
        #self.can3_result.setText(f"Nichole received {self.can1_total} : {vote_percent3}")
        #self.can4_result.setText(f"{custom_candiate} recieved ")

        self.can1_result.setText("Bianca received {self.can1_total} : {vote_percent1}")
        self.can2_result.setText("Jack received {self.can1_total} : {vote_percent2}")
        self.can3_result.setText("Nichole received {self.can1_total} : {vote_percent3}")
        self.can4_result.setText("{custom_candidate} received ")

        self.overall_results_label.setText("{Candidate} Wins")



