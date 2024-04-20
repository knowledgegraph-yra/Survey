---
marp: true
size: 4:3
paginate: true
style: |
  section {
    font-size: 12px; /* Adjust font size to fit content */
    margin: 0;
    padding: 20px 40px;
  }
  h2 {
    margin: 0;
    padding: 0;
  }
  p {
    margin: 0;
    padding: 0;
  }
---


# ASKRL: An Aligned-Spatial Knowledge Representation Learning Framework for Open-world Knowledge Graph

## 一言でいうと
オープンワールド知識グラフにおけるゼロショットエンティティの問題に対処 
## 著者/所属機関
Ziyu Shang, Peng Wang, Yuzhang Liu, Jiajun Liu and Wenjun Ke
- School of Computer Science and Engineering, Southeast University, Nanjing, China

## DOI
[10.1007/978-3-031-47240-4_6](https://doi.org/10.1007/978-3-031-47240-4_6)
## 会議名(ジャーナル名)  
The 22nd International Semantic Web Conference (ISWC2023)
## トラック
Research Track

## 動機
クローズドワールド知識表現学習(KRL)モデルは、ゼロショットエンティティを効果的に処理できず、オープンワールド設定での使用に限界 
## 手法
SKRLは、構造化された埋め込み層、説明エンコーディング層、そして埋め込み空間整列層の3つの主要なコンポーネントで構成． エンティティとリレーションの表現を構造化された空間と意味空間の両方で学習 
## 背景
オープンワールド知識グラフは、新たなエンティティやリレーションが継続的に追加されるため、既存のKRLモデルでは対応できない  

## 結果
ASKRLはオープンワールド知識グラフ完了データセットにおいて、強力なベースラインモデルを一貫して上回る．特にBERTベースのエンコーダの際に顕著な向上 

## 考察
KRLモデルやトランスフォーマーベースのエンコーダーを使用することで、さらなる改善が期待  

## 課題
 異なる種類の知識グラフにおけるASKRLの適用性，多言語や他ドメインでの実験 

## 読んだ範囲
斜め読み程度


---

# FORECASTTKGQUESTIONS: A Benchmark for Temporal Question Answering and Forecasting over Temporal Knowledge Graphs

## 一言でいうと
未来についての質問に答える時間的KG質問応答(TKGQA)タスクのベンチマークデータセットForecastTKGQuestionsと予測TKGQAタスクの提案

## 著者/所属機関
Zifeng Ding<sup>1,2</sup>, Zongyue Li<sup>1,3</sup>, Ruoxia Qi<sup>1</sup>, Jingpei Wu<sup>1</sup>, Bailan He<sup>1,2</sup>, Yunpu Ma<sup>1,2</sup>, Zhao Meng<sup>4</sup>, Shuo Chen<sup>1,2</sup>, Ruotong Liao<sup>1,2</sup>, Zhen Han<sup>1</sup>, and Volker Tresp<sup>1</sup>
1. LMU Munich, Germany. 
2. Siemens AG, Germany.
3. Munich Center for Machine Learning (MCML), Germany. 
4. ETH Zurich, Switzerland

## DOI
https://doi.org/10.1007/978-3-031-47240-4_29

## 会議名(ジャーナル名)  
The 22nd International Semantic Web Conference (ISWC2023)

## トラック
Research Track

## 動機
最近のTKG補完は未来のタイムスタンプでの予測に注⽬

## 手法
エンティティ予測質問、Yes-unknown質問、ファクト推論質問の三種類を含むTKG予測モデルTANGOとBERTを採⽤した提案モデルForcastTKGQA

## 背景
既存のTKGQA研究は未来の事実の予測を対象としていない

## 結果
提案モデルがSOTA。TKGQA予測においてはTKG予測モデルがTKG補完モデルよりも有効︖→有効。データセットは解答可能︖→GTのTKG情報があれば可。データセットは効率的︖→データ増加するほど精度が向上するため効率的

## 考察
⼈間と⽐較するとまだ改善の余地が⼤きい。

## 課題
質問タイムスタンプt_qにおけるGTのTKG情報𝒢_{t_q}を正確に推論。効果的なマルチホップ推論。より良いファクト推論のためのTKGQAモデル開発。

## 読んだ範囲
斜め読み程度
