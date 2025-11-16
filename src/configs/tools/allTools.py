from configs.tools.memoryToolsSet import MemoryToolset
from configs.tools.bookToolSet import BookToolSet
from configs.tools.usersToolsSet import UserToolSet

mainTools = [
	MemoryToolset().getMemoryContext,
	BookToolSet().countBooks,
	BookToolSet().countByFormat,
	BookToolSet().countByGenre,
	BookToolSet().countBySubgenre,
    BookToolSet().getFormats,
    BookToolSet().getGenres,
    BookToolSet().getSubgenres,
    BookToolSet().getLanguages,
    BookToolSet().getLevels,
	BookToolSet().getBooksByTitle,
    BookToolSet().getBooksByGenre,
    BookToolSet().getBooksBySubgenre,
    BookToolSet().getBooksByLanguage,
    BookToolSet().getBooksByLevel,
    BookToolSet().getBooksByTheme,
    BookToolSet().getBooksByFiltering,
    BookToolSet().getIntelligenceBook,
    BookToolSet().getAllBooksByLevel,
	UserToolSet().getUserCategories,
	UserToolSet().getUserFormats,
	UserToolSet().getUserPreferences,
]