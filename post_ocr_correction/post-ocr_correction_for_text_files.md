# How to do a post-OCR correction for TEXT files

After the ocerisation of a corpus, a correction is always necessary, since an OCR software is never 100% accurate in its transcription.
When using eScriptorium, the correction is usually made on XML files (as it is explained [here](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/blob/master/post_ocr_correction/how_to_do_a_transcription_(with_eScriptorium).md)) but with other softwares, you can need to do it with TEXT files.
The goal of this document is to present the steps to follow to correct your corpus, by using the available scripts.

1. The texts that need to be corrected are all in the same folder
1. A new folder has to be created : it will contain the python dictionaries that will be generated by the first script
1. Search wrongly transcribed and incorrect words in your TEXT files by executing this [script](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/blob/master/post_ocr_correction/scripts/spellcheck_texts_TEXT.py) 
(**Attention : the only dictionary available in the repository is for french texts. To work with other languages, you can download new dictionnaries [here](https://github.com/hermitdave/FrequencyWords) but you will have to transform the TEXT file in JSON.**)
1. Correct the produced dictionaries manually and by using the corresponding images of the texts
1. Integrate every dictionary in a single file entitled *dictionary* (as it is named in the next script)
1. Apply the corrections from the dictionary by using the corresponding [script](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/blob/master/post_ocr_correction/scripts/text_correction_TEXT.py) for TEXT files
1. Correct manually the remaining errors in the text, like in step 4