# In-Use Track用テンプレート案
(https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008032 より)  
(https://iswc2021.semanticweb.org/in-use-call) も参考
# 論文タイトル                                                                                                                                                                         
## 著者名
著者名(所属), 著者名(所属), ... 
Yulia Svetashova(Bosch Corporate Research/Karlsruhe Institute of Technology), Baifan Zhou(Bosch Corporate Research/Karlsruhe Institute of Technology), Tim Pychynski(Bosch Corporate Research), Stefan Schmidt(Bosch Corporate Research), York Sure-Vetter(Karlsruhe Institute of Technology), Ralf Mikut(Karlsruhe Institute of Technology), Evgeny Kharlamov(Bosch Center for Artificial Intelligence/University of Oslo)
## DOI
(https://doi.org/10.1007/978-3-030-62466-8_33)[https://doi.org/10.1007/978-3-030-62466-8_33]
## 会議名(ジャーナル名)                                                                                                                                                         
The 19th International Semantic Web Conference (ISWC2020)
## トラック                                                                                                                                                              
In-Use
## 動機
自動車産業では溶接の品質モニタリングが重要であり，Boschではそのための機械学習ワークフローを採用している。しかし、複雑でコストがかかり、コミュニケーション、データ統合、ML品質モデルの汎用性の課題があるため解決したい。
## 手法
従来の機械学習ワークフローをセマンティックコンポーネントで拡張したSemMLと呼ばれるシステムを開発。セマンティックコンポーネントは  
- Ontology extender: テンプレートを埋めることで専門家に上位オントロジーの観点でドメインを記述できるようにする  
- Domain knowledge annotator: アノテーションにより生データをドメインオントロジーにマッピングすることでデータ統合  
- Machine learning annotator: 自動推論によりマッピングからML関連情報の推論、各生データソースごとにMLオントロジーとデータ間のマッピングを作成  
- Ontology interpreter: MLモデルと生データの統一化された説明可能な検査を可能にする
## 背景
- 機械学習ワークフローの促進においてセマンティック技術の利用をカバーした様々な研究が存在しているが、著者らの要求を部分的にしか満たさない。
- 製造業の品質分析を支援するために独自にオントロジーやテンプレートを開発してワークフローに統合する必要があるが、既存のものは著者らのドメインを十分にカバーしない。
- 既存のオントロジー拡張ツールはかなり調整が必要であり、MLワークフローや著者らのインフラと用意に統合できないので独自のオントロジー拡張ツールを開発した。
## 結果
(4) What do the results show (figures and data tables)?
## 利用実績
(5) How did the author(s) interpret the results (interpretation/discussion)?  
## 学んだ教訓やベストプラクティス
(5) How did the author(s) interpret the results (interpretation/discussion)?  
