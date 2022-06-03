# Pipeline for digital scholarly editions

## What is the pipeline for digital scholarly editions?
Born from the DAHN project, a technological and scientific collaboration between Inria, Le Mans Université and EHESS, and funded by the French Ministry of Higher Education, Research and Innovation (more information on this project can be found [here](https://github.com/FloChiff/DAHNProject)), the pipeline aims at reaching the following goal: facilitate the digitization of data extracted from archival collections, and their dissemination to the public in the form of digital documents in various formats and/or as an online edition.  
This pipeline has been created by [Floriane Chiffoleau](https://cv.archives-ouvertes.fr/floriane-chiffoleau), under the supervision of [Anne Baillot](https://cv.archives-ouvertes.fr/annebaillot) and [Laurent Romary](https://cv.archives-ouvertes.fr/laurentromary), and with the help of [Alix Chagué](https://cv.archives-ouvertes.fr/alix-chague) and [Manon Ovide](https://github.com/inoblivionem).

---

## Schematic representation of the pipeline
![Pipeline for digital scholarly editions](https://raw.githubusercontent.com/DiScholEd/pipeline-digital-scholarly-editions/master/pipeline.png)

---

## The steps
As the previously showned schema demonstrated it, the pipeline for digital scholarly editions is made of six steps: digitization, segmentation, transcription, post-OCR correction, encoding and publication. Each of this steps requires interface, tools, scripts and documentation. Every element required to execute each phase is presented below.

### Digitization
Every publication project starts with a collection of papers. Even though the digital format of those papers (PDF, PNG, JPG, TIFF, etc.) does not matter for the process that they will go through afterwards, having those papers in a sustainable and interoperable state is preferable.  
Consequently, the digitization phase relies on the [IIIF (International Image Interoperability Framework)](https://iiif.io/) format to host images for the exploited corpus. Many IIIF servers exist to host images, some conservation sites have their own and they can upload some of their archives on it but it is not systematic. Therefore, in addition to the information given to add IIIF links to the future TEI XML files of the corpus, this pipeline proposes an easy-to-use and open-source (French) IIIF server.

- [NAKALA](https://nakala.fr/) --> To be able to use it, it is required that you create a Huma-Num account
- [Documentation NAKALA](https://documentation.huma-num.fr/nakala/)
- [Scripts](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/tree/master/digitization/scripts) for the execution of this step, going from gathering the metadata for the upload on NAKALA to adding the IIIF links to the TEI XML encoded files
- [Documentation](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/blob/master/digitization/how_to_add_IIIF_links_to_XML_files.md) explaining how to run the scripts
- Blog post about the development of this step : _[Availability and high quality: distributing the facsimile with NAKALA](https://digitalintellectuals.hypotheses.org/4294)_

### Segmentation/Transcription
To obtain a machine-readable version of a collection of papers, it needs to go through the process of segmentation and transcription. Every page of the collection have to be segmented, i.e. have the layout and every line identified, and then transcribed, i.e. have the text contained by those lines recognized.  
Many tools created to execute this specific task can be found online (some free and some not) but we chose a specific one for this step, because of the many advantages it brings. Firstly, it is not in command line but works with an interface, so it is easier to use for a beginner. Secondly, it works for printed, typewritten and handwritten texts. Thirdly, it does not only allow the user to segment/transcribe, it also proposes to train your own model with your own _ground truth_. Finally, this tool comes with an extended link to the digital humanities community, which offers ways to improve the experience with the chosen tool.

- [Kraken](https://kraken.re/master/index.html) --> It is the OCR system we are relying on to do this step
- [eScriptorium](https://escriptorium.paris.inria.fr/) --> This interface is an alternative to CLI transcription. To be able to use it, it is required to get an account.
- [Documentation](https://lectaurep.hypotheses.org/documentation/escriptorium-tutorial-en) eScriptorium
- [HTR-United](https://htr-united.github.io/): GitHub organization gathering ground truth of all periods and style of writing, mostly but not exclusively in French to rapidly train models on smaller corpora
- [Documentation](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/blob/master/segmentation_transcription/how_to_do_a_transcription_(with_eScriptorium).md) on how to do a transcription (using eScriptorium)
- [Examples](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/tree/master/segmentation_transcription/examples) of models of segmentation and transcription and their logs 
- Blog posts about the development of this step : 
    - _[How to produce a model for the transcription](https://digitalintellectuals.hypotheses.org/3702)_
    - _[Difficulties in creating the transcription model](https://digitalintellectuals.hypotheses.org/3812)_
    - _[How to produce a model for the segmentation](https://digitalintellectuals.hypotheses.org/3844)_
    - _[Transcribing the corpus](https://digitalintellectuals.hypotheses.org/3872)_

### Post-OCR correction
The process of text recognition is not perfect. Even with a highly accurate model, there are often errors still present in the transcription. This step has been created in order to speed up the process of correcting those errors.  
![Schema of post-OCR correction](https://raw.githubusercontent.com/DiScholEd/pipeline-digital-scholarly-editions/master/post_ocr_correction/schema_post_ocr_correction.png)

- [Pyspellchecker](https://github.com/barrust/pyspellchecker) --> It is the module used for spell checking the transcriptions
- [Scripts](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/tree/master/post_ocr_correction/scripts) to check for errors and subsequently correct it, available for Page XML, XML Alto and TEXT files
- [Documentation](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/blob/master/post_ocr_correction/how_to_do_a_transcription_(with_eScriptorium).md) on how to do a transcription (using eScriptorium) (same as the one in the previous step)
- Repository containing frequency words for a large selection of languages : [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords/tree/master/content)
- Blog post about the development of this step : _[Transcribing the corpus](https://digitalintellectuals.hypotheses.org/3872)_

### Encoding
- [The TEI Guidelines](https://tei-c.org/release/doc/tei-p5-doc/en/html/index.html)
- [Page2tei](https://github.com/TEI4HTR/page2tei): GitHub repostiory for the transformation of a PAGE XML file into XML-TEI format
- [Scripts](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/tree/master/encoding/scripts) for the encoding of TEXT files, for the metadata, the body and the named entities
- [Documentation](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/tree/master/encoding/documentation) on how to use the various scripts mentioned before
- [Guidelines](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/tree/master/encoding/guidelines) for the encoding of ego documents 
- Blog posts about the development of this step : 
    - _[Encoding an XML Tree model for my corpus](https://digitalintellectuals.hypotheses.org/3360)_
    - _[Encoding the corpus](https://digitalintellectuals.hypotheses.org/3891)_
    - _[Recognizing and encoding the corpus’ named entities](https://digitalintellectuals.hypotheses.org/4470)_

### Publication
- [eXist-db](http://exist-db.org/exist/apps/homepage/index.html) --> servor hosting TEI Publisher's platforms
- [TEI Publisher](https://teipublisher.com/index.html)
- [Documentation](https://teipublisher.com/exist/apps/tei-publisher/doc/documentation.xml?odd=docbook.odd) of TEI Publisher
- Schema of how the TEI processing model works: 
![TEI processing model](https://raw.githubusercontent.com/DiScholEd/pipeline-digital-scholarly-editions/master/publication/teiprocessingmodel.png)
- [Digital Scholarly Editions (DiScholEd)](https://discholed.huma-num.fr/exist/apps/discholed/index.html) --> Application created for the publication of the corpora worked on to establish this pipeline
- [Documentation](https://github.com/DiScholEd/pipeline-digital-scholarly-editions/blob/master/publication/documentation_DiScholEd.xml) of the composition and running of DiScholEd
- Blog posts about the development of this step : 
    - _[Publication of my digital edition – Working with TEI Publisher](https://digitalintellectuals.hypotheses.org/3912)_
    - _[Publication of my digital edition – Developing my TEI Publisher application](https://digitalintellectuals.hypotheses.org/4173)_
    - _[Publication of my digital edition – Online launch of the TEI Publisher application](https://digitalintellectuals.hypotheses.org/4399)_

## Communications
During the development of the pipeline and the creation of its components, I took part in multiple conferences on digital humanities and other related topics, during which I presented the pipeline and its steps, according to its state of advancement. Here are the list of conferences in which I gave a presentation, as well as some of the publications I made afterwards.

### Conferences
- "Le projet DAHN, production d’une chaîne d’édition scientifique numérique pour un corpus d’égodocuments", _Journées EVEille 2021, Journée 2 : Bibliothèques numériques_, 12/02/2021 : [https://eveille.hypotheses.org/journees-eveille-2021](https://eveille.hypotheses.org/journees-eveille-2021)
- "DAHN: An accessible and transparent pipeline for publishing historical egodocuments ", _What's Past is Prologue: The NewsEye International Conference 2021_, 17/03/2021 : [https://www.newseye.eu/blog/news/the-newseye-international-conference/](https://www.newseye.eu/blog/news/the-newseye-international-conference/)
- "A TEI-based publication pipeline for historical egodocuments -the DAHN project", _Next Gen TEI, 2021 - TEI Conference and Members’ Meeting_, 26/10/2021 : [https://tei-c.org/next-gen-tei-2021/](https://tei-c.org/next-gen-tei-2021/)
- "Penser la réutilisabilité patrimoniale : présentation de la pipeline d'édition numérique de documents d'archives du projet DAHN", _Humanistica 2022_, 20/05/2022 : [https://humanistica2022.sciencesconf.org](https://humanistica2022.sciencesconf.org)

### Publications
- Alix Chagué, Floriane Chiffoleau. "An accessible and transparent pipeline for publishing historical egodocuments." _WPIP21 - What's Past is Prologue: The NewsEye International Conference_, Mar 2021, Virtual, Austria. ⟨[hal-03173038](https://hal.archives-ouvertes.fr/hal-03173038)⟩
- Floriane Chiffoleau, DAHN Project category, _Digital Intellectuals Blog_, 2020-2021: [https://digitalintellectuals.hypotheses.org/category/dahn](https://digitalintellectuals.hypotheses.org/category/dahn)
- Floriane Chiffoleau, Anne Baillot, Manon Ovide. "A TEI-based publication pipeline for historical egodocuments -the DAHN project." _Next Gen TEI, 2021 - TEI Conference and Members’ Meeting_, Oct 2021, Virtual, United States. ⟨[hal-03451421](https://hal.archives-ouvertes.fr/hal-03451421)⟩
- Floriane Chiffoleau, Anne Baillot. "Le projet DAHN : une pipeline pour l'édition numérique de documents d'archives." 2022. ⟨[hal-03628094](https://hal.archives-ouvertes.fr/hal-03628094)⟩