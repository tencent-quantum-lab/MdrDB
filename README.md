# MdrDB: Mutation-induced drug resistance DataBase

MdrDB is a database of information related to changes in protein-ligand affinity caused by mutations in protein structure. It brings together wild type protein-ligand complexes, mutant protein-ligand complexes, binding affinity changes upon mutation (ΔΔG), and biochemical features of complexes to advance our understanding of mutation-induced drug resistance, the development of combination therapies, and the discovery of novel chemicals.

![workflow_0624](https://github.com/tencent-quantum-lab/MdrDB/blob/main/figure/workflow_0624.png)



## 📌 News 📌

**Current release:** MdrDB v.1.0. 2022 contains 100537 samples, generated from 240 proteins (5119 total PDB structures), 2503 mutations, and 440 drugs. 95971 samples are based on available PDB structures, and 4566 samples are based on AlphaFold2 predicted structures.

All data is available to browse and download on the MdrDB website: https://quantum.tencent.com/mdrdb/.

A full tutorial for MdrDB is available at: https://quantum.tencent.com/mdrdb/tutorial/.



## Content list

In the paper, we conducted three scenarios to test whether using MdrDB\_CoreSet as the training dataset (using 146 calculated biochemical features) can improve the model generalization performance in predicting mutation-induced drug resistance in the TKI dataset.

You can try the code and obtain the results from this repo:

- ***Data:*** contains meta data and processed biochemical features from MdrDB\_CoreSet.

- ***Demo:*** contains the source code of multiple machine learning methods on different training datasets: Platinum (no tyrosine kinase), Platinum, and MdrDB\_CoreSet (Single substitution), and then test on the TKI dataset to predict tyrosine kinase inhibitors affinity change values.

- ***Results:*** contains prediction results and plotted figures.

***Update (2023.05.12)***

Furthermore, we also provide a comprehensive evaluation of 10 machine learning models in several different scenarios, and provide baseline prediction results on the MdrDB database. It is our hope that this will help further the development of new machine learning algorithms using the MdrDB database and facilitate drug resistance research. The source code is available at: `MdrDB_ML_baselines.ipynb`.



## Example output



![Fig4_barplot](https://github.com/tencent-quantum-lab/MdrDB/blob/main/figure/Fig4_barplot.png)



## Citation of database

```
@article{yang2022mdrdb,
  title={MdrDB: Mutation-induced drug resistance DataBase},
  author={Yang, Ziyi and Ye, Zhaofeng and Qiu, Jiezhong and Feng, Rongjun and Li, Danyu and Hsieh, Changyu and Allcock, Jonathan and Zhang, Shengyu},
  pages={2022--10},
  journal={bioRxiv},
  year={2022},
  publisher={Cold Spring Harbor Laboratory}
}
```
