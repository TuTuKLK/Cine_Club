from PySide2 import QtWidgets, QtCore
from movie import get_movies
from movie import Movie



class App(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Ciné Club")
    self.setup_ui()
    self.populate_movies()
    self.setup_connections()
    self.resize(250,300)



  def setup_ui(self):
    self.main_layout = QtWidgets.QVBoxLayout(self)

    self.le_name_movie = QtWidgets.QLineEdit()
    self.btn_add_movie = QtWidgets.QPushButton("Ajouter un film")
    self.lw_list_movies = QtWidgets.QListWidget()
    self.lw_list_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)  # type: ignore
    self.btn_remove_movies = QtWidgets.QPushButton("Supprimer le(s) film(s)")

    self.main_layout.addWidget(self.le_name_movie)
    self.main_layout.addWidget(self.btn_add_movie)
    self.main_layout.addWidget(self.lw_list_movies)
    self.main_layout.addWidget(self.btn_remove_movies)

  def populate_movies(self):
    movies = get_movies()

    for movie in movies:
      lw_item = QtWidgets.QListWidgetItem(movie.title)
      lw_item.setData(QtCore.Qt.UserRole, movie) # type: ignore
      self.lw_list_movies.addItem(lw_item)  # type: ignore

  def setup_connections(self):
    self.btn_add_movie.clicked.connect(self.add_movie)  # type: ignore
    self.btn_remove_movies.clicked.connect(self.remove_movies)  # type: ignore
    self.le_name_movie.returnPressed.connect(self.add_movie)  # type: ignore


  def add_movie(self):
    movie_title = self.le_name_movie.text()
    if not movie_title:
      return False
    movie = Movie(title=movie_title)
    resultat = movie.add_to_movies()
    if resultat:
      lw_item = QtWidgets.QListWidgetItem(movie.title)
      lw_item.setData(QtCore.Qt.UserRole, movie) # type: ignore
      self.lw_list_movies.addItem(lw_item)  # type: ignore
    self.le_name_movie.setText("")


  def remove_movies(self):
    for selected_item in self.lw_list_movies.selectedItems():
      movie = selected_item.data(QtCore.Qt.UserRole)
      movie.remove_from_movies()
      self.lw_list_movies.takeItem(self.lw_list_movies.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()

