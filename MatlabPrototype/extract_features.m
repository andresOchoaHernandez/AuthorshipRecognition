function feature_vector = extract_features(path)
tic
book = extractFileText(path);
%%CHAR STATISTICS
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
counts_alphabet = zeros(1,size(alphabet,2));

punctuation = ['?',',','!','.',':',';'];
counts_punctuation = zeros(1,size(punctuation,2));

chars = lower(book);

%removing some unusefull stuff
chars = strtrim(chars);
chars = erase(chars,newline);
chars = erase(chars,char(13));
chars = erase(chars," ");

chars = split(chars,"")';
chars = tokenizedDocument(chars);
chars = removeEmptyDocuments(chars);
tdetails = tokenDetails(chars);

tot_chars = 0;
for i=1:size(alphabet,2)
    counts_alphabet(i)=sum(tdetails.Token == alphabet(i))/size(tdetails,1);
    tot_chars = tot_chars + sum(tdetails.Token == alphabet(i));
end
for i=1:size(punctuation,2)
    counts_punctuation(i)=sum(tdetails.Token == punctuation(i))/sum(tdetails.Type == 'punctuation');
end
clearvars -except book alphabet counts_alphabet punctuation counts_punctuation tot_chars
%%PART OF SPEECH, SENTENCE AND WORD STATISTICS
function_words = ["determiner" "adposition" "pronoun" "auxiliary-verb" "adverb" "coord-conjunction" "subord-conjunction"];
nouns = ["noun" "proper-noun"];
parts_of_speech = [function_words nouns "adjective" "verb"];
pos_counts = zeros(1,size(parts_of_speech,2));

pos = tokenizedDocument(book);
pos = addPartOfSpeechDetails(pos);
tdetails = tokenDetails(pos);

for i = 1 : size(parts_of_speech,2)
    pos_counts(i) = sum(tdetails.PartOfSpeech == parts_of_speech(i))/size(tdetails,1);
end

lexical_variety = sum(tdetails.PartOfSpeech == "noun" | ...
                      tdetails.PartOfSpeech == "proper-noun" | ...
                      tdetails.PartOfSpeech == "adjective" | ... 
                      tdetails.PartOfSpeech == "verb" | ... 
                      tdetails.PartOfSpeech == "adverb")/size(tdetails,1);
                  
average_sentence_length = size(tdetails,1)/max(tdetails.SentenceNumber);
average_word_length = tot_chars / size(tdetails,1);
tot_words = size(tdetails,1);

feature_vector = [counts_alphabet counts_punctuation pos_counts lexical_variety average_sentence_length average_word_length tot_words]';
toc
end
