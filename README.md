# Master Thesis
## Low-Resource Neural Machine Translation for Nagamese to English. 
Nagamese is an Assamese-lexified creole language spoken natively in the Northeastern Indian state of Nagaland and it functions as the lingua franca of the state. It is considered a low-resource language i.e. a language that has limited availability of linguistic resources, such as written text, audio recordings, and computational tools, as well as a lack of research and development efforts compared to more widely spoken languages.

## Tasks
- [x] Scrape English & Nagamese text from the Bible website.
- [ ] Scrape Nagamese text from Nagamese Khobor. (ongoing)
- [x] Create a parallel corpus for Nagamese-English.
- [x] Train baseline models for Nagamese-English & English-Nagamese.
- [x] Fine-tune mBART-50 on the dataset.
- [x] Fine-tune M2M-100 on the dataset.
- [x] Fine-tune NLLB-200 on the dataset.

## Results
  BLEU Scores
|**Model**| **eng-naga**| **naga-eng** | **eng-naga JD**| **naga-eng JD** |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| **Transformer**  | 12.08 | 14.77 | 10.05 | 18.39 |
| **mBART-50**  | 21.45 | 27.92 | 25.61 | 29.48 | 
| **M2M-100** | 23.51 | 30.42 | 34.76 | 33.87 |
| **NLLB-200** | 19.58 | 38.98 | 21.43 | 40.29 |

## References
- [Machine Translation Models: How to Build and Deploy](https://blog.machinetranslation.io/opennmt-tutorial/) by Yasmin Moslem.
- [Translation](https://huggingface.co/learn/nlp-course/chapter7/4?fw=tf) by Hugging Face.
- [Multilingual Denoising Pre-training for Neural Machine Translation](https://arxiv.org/abs/2001.08210)
- [Beyond English-Centric Multilingual Machine Translation](https://arxiv.org/abs/2010.11125)
- [No Language Left Behind: Scaling Human-Centered Machine Translation](https://arxiv.org/abs/2207.04672)
