import json
from fastavro import writer, parse_schema

# Define the Avro schema
schema = {
    "type": "record",
    "name": "BibleVerse",
    "fields": [
        {"name": "Version", "type": "string"},
        {"name": "Book", "type": "string"},
        {"name": "BookNumber", "type": "int"},
        {"name": "Testament", "type": "string"},
        {"name": "ChapterNumber", "type": "int"},
        {"name": "VerseNumber", "type": "int"},
        {"name": "Verse", "type": "string"},
        {"name": "Embedding", "type": "string"}
    ]
}

# Define the order of books in the Bible
books_order = [
    # Old Testament
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth", 
    "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", 
    "Nehemiah", "Esther", "Job", "Psalms", "Proverbs", "Ecclesiastes", "Song of Solomon", 
    "Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", 
    "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", 
    "Malachi",
    # New Testament
    "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", 
    "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", 
    "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", 
    "1 John", "2 John", "3 John", "Jude", "Revelation"
]

# Load the JSON data
with open('NKJV_bible.json', 'r') as f:
    data = json.load(f)

# Correct book names if needed
def correct_book_name(book_name):
    corrections = {
        "Psalm": "Psalms"
    }
    return corrections.get(book_name, book_name)

# Determine if a book is in the Old or New Testament
def get_testament(book_name):
    old_testament_books = set(books_order[:39])
    return "Old Testament" if book_name in old_testament_books else "New Testament"

# Transform the data into the desired format
records = []
for book in data['books']:
    book_name = correct_book_name(book['name'])
    book_number = books_order.index(book_name) + 1
    testament = get_testament(book_name)
    for chapter in book['chapters']:
        chapter_num = chapter['num']
        for verse in chapter['verses']:
            verse_num = verse['num']
            verse_text = verse['text']
            embedding = (
                f"<version>{data['version']}</version>"
                f"<book>{book_name}</book>"
                f"<booknumber>{book_number}</booknumber>"
                f"<testament>{testament}</testament>"
                f"<chapternumber>{chapter_num}</chapternumber>"
                f"<versenumber>{verse_num}</versenumber>"
                f"<verse>{verse_text}</verse>"
            )
            records.append({
                "Version": data['version'],
                "Book": book_name,
                "BookNumber": book_number,
                "Testament": testament,
                "ChapterNumber": chapter_num,
                "VerseNumber": verse_num,
                "Verse": verse_text,
                "Embedding": embedding
            })

# Write the records to an Avro file
output_file = 'bible_verses_enhanced.avro'
with open(output_file, 'wb') as out:
    writer(out, parse_schema(schema), records)

print(f"Data has been written to {output_file}")
