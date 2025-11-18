from configs.tools.bookToolSet import BookToolSet
from configs.tools.usersToolsSet import UserToolSet

mainTools = [
	BookToolSet().countBooks,
	BookToolSet().countByFormat,
	BookToolSet().countByGenre,
	BookToolSet().countBySubgenre,
    BookToolSet().getFormats,
    BookToolSet().getGenres,
    BookToolSet().getSubgenres,
    BookToolSet().getThemes,
    BookToolSet().getLanguages,
    BookToolSet().getLevels,
	BookToolSet().getBooksByTitle,
    BookToolSet().getBooksByLanguage,
    BookToolSet().getBooksByLevel,
    BookToolSet().getBooksByFiltering,
    BookToolSet().getIntelligenceBook,
    BookToolSet().getAllBooksByLevel,
	UserToolSet().getUserCategories,
	UserToolSet().getUserFormats,
	UserToolSet().getUserPreferences,
]