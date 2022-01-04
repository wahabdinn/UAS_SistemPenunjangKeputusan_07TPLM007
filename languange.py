from langdetect import detect

all_languages_codes =   {
            'id': 'Indonesian',
            'ind': 'Indonesian',
            'en': 'English',
            'ja': 'Japanese',
            'eng': 'English',
            'jpn': 'Japanese'
}

input_sentences = ["That's thirty minutes away. I'll be there in ten.",
                   "Itu tiga puluh menit lagi. Saya akan berada di sana dalam sepuluh.",
                   "「あと30分です。10分で到着します。」、"
]

lemmatizer_names = ["Language Code", "Input Sentence"]
format_text = '{:24}' * (len(lemmatizer_names) + 1)
print ('\n', format_text.format("Language Name", *lemmatizer_names),'\n','='*120)
for data in input_sentences:
    language_code = detect(data)    
    sentence = [all_languages_codes.get(language_code), language_code, data]
    print (format_text.format(*sentence))