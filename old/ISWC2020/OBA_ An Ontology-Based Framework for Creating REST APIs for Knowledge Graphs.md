# OBA: An Ontology-Based Framework for Creating REST APIs for Knowledge Graphs
## 一言で言うと
オントロジーを入力として与えると、KGに対してリソース取得/編集/追加/削除可能なJSON-based REST APIサーバを生成するフレームワーク

## 著者名
Daniel Garijo and Maximiliano Osorio (Information Sciences Institute, University of Southern California, Los Angeles, USA)
## DOI
[https://doi.org/10.1007/978-3-030-62466-8_4](https://doi.org/10.1007/978-3-030-62466-8_4)
## 会議名
The 19th International Semantic Web Conference (ISWC2020)
## トラック
Resources Track
## Resource Type
Software

# Resources Trackの視点

## 動機
- KGを活用するWebシステムの開発において、オントロジエンジニアとWeb開発者でギャップがあり、後者にはオントロジーなどの知識が無い
- 目的：それらの知識が無くてもKGの中身にアクセスできる仕組み

## リソースの設計方針
- [Ontology-Based APIs (OBA) framework](https://github.com/KnowledgeCaptureAndDiscovery/OBA/)
    - オントロジーを入力として与えると、KGに対してリソース取得/編集/追加/削除可能なJSON-based REST APIサーバを生成
- 貢献
    - OWLオントロジーからREST Open API Specification(OAS)を自動生成する手法
    - OASに基づいて、ターゲットのKGに対するリクエストを自動で制御するサーバ実装を生成するフレームワーク
        - その実装は、そのAPIにポストされたリソースをvalidateし、OASで定義されたJSONフォーマってで結果を返す
    - SPARQL endpointから返ってきたJSON-LDを、OASで定義されたフォーマットに応じてJSONに変換する手法
    - ユーザーが、POSTリクエストを通してKGに貢献するための、named graphに基づくメカニズム
    - KGに対するAPIの検証テストを自動生成

## 新規性
- OBAは以下を実現するが、そういうものは過去にはない。
    - KGの内容の概要を、Web開発者にとっても理解しやすい一般的な形式(OAS)で提供（[W3C Linked Platform](http://www.w3.org/TR/2015/REC-ldp-20150226/)とその実装([Apache Marmotta](http://marmotta.apache.org/), [TrellisLDP](https://www.trellisldp.org/about.html))、[Linked Data Templates](https://atomgraph.github.io/Linked-Data-Templates/)は、Web開発者に分かる形でKGの内容の概要を提供しない）
    - ポストされるリソースはOpenAPIスキーマでvalidateされる。APIは、自動でオントロジーから生成。全ての結果は、生成されるOASに応じて、JSONで返される。（Basil, [GRLC](https://doi.org/10.1007/978-3-319-47602-5_48), [r4r](https://github.com/oeg-upm/r4r), [RAMOSE](https://github.com/opencitations/ramose)は、KGへのアクセスを簡単にするために、SPARQLクエリからREST APIを作成するが、POSTされたデータのValidationが必要だし、手動でのクエリ定義が必要で、JSON形式への変換も必要）
    - KG内のデータをクエリするために使用される、基礎となるオントロジーに精通している必要がない（[SPARQL transformer](https://doi.org/10.1007/978-3-030-30796-7_28), [SPARQL-JSONLD](https://github.com/usc-isi-i2/sparql-jsonld)、\[14\]は、Web開発者がKG内のデータをクエリするために使用される、基礎となるオントロジーに精通している必要がある）
    - OBAはAPIサーバを構築するための実装を提供（[owl2oas](https://github.com/hammar/owl2oas)はサーバ構築は未提供）
    - オントロジーを、KGの「内容」をexploitするためにAPIを生成するためのtemplateとして、ontologyを使っている。（[\[4\]](https://doi.org/10.5220/0005987201500157) は、オントロジーの「クラス」や「プロパティ」へアクセスするREST APIを定義）

## リソースの再利用性/活用実績
- Usage Examples: 三つの事例で、フレームワークの各要素をデモンストレーション。

## 品質
- Performance Analyses
    1. 結果をJSONに変換する際の、OBAによるオーバーヘッド　→　barely noticeable
    1. 毎秒の多重リクエスト応答のためのAPIの性能
        - reverse proxy cachingが有効であれば、60 queries/sec を200ms以下の遅延で制御可能。
        - cache無しの場合、10 queries/sec 以上でパフォーマンスが低下。使用するサーバの構成で改善可能かもしれない。
- Usage Examples: 三つの事例においても、ベストプラクティスな手法である。

## リソースの可用性
- GitHub: https://github.com/KnowledgeCaptureAndDiscovery/OBA/
- ライセンス仕様: Apache License 2.0 https://github.com/KnowledgeCaptureAndDiscovery/OBA/blob/master/LICENSE
- 持続可能性計画、中長期的なメンテナンスの計画
- オープンスタンダードの採用:
  - [OpenAPI Specification](https://spec.openapis.org/oas/v3.0.3)
  - OWL, JSON-LD, SPARQLなどのW3C standardsに準拠

## 次にすべきこと
- 以下は投稿時点で対応作業中
    - OWLとOAS間のmappingにおいて、複雑なaxiomatizationへの対応
        - propertyのrangeにunionとintersectionが同時に出てくる場合など
    - JSON-LDリクエストへの対応
- GraphQLへの追加対応も検討中
- 最も一般的なデータパターンでAPIを公開するために、オントロジーを既存のKGパターンマイニングツールと組み合わせる


## 読んだ範囲
斜め読み程度

---
# Research Trackの視点

## (1) What do the author(s) want to know (motivation)?

- KGを活用するWebシステムの開発において、オントロジエンジニアとWeb開発者でギャップがあり、後者にはオントロジーなどの知識が無い
- それらの知識が無くてもKGの中身にアクセスできる仕組み

## (2) What did they do (approach/methods)?
- [Ontology-Based APIs (OBA) framework](https://github.com/KnowledgeCaptureAndDiscovery/OBA/)
    - オントロジーを入力として与えると、KGに対してリソース取得/編集/追加/削除可能なJSON-based REST APIサーバを生成
- 貢献
    - OWLオントロジーからREST Open API Specification(OAS)を自動生成する手法
    - OASに基づいて、ターゲットのKGに対するリクエストを自動で制御するサーバ実装を生成するフレームワーク
        - その実装は、そのAPIにポストされたリソースをvalidateし、OASで定義されたJSONフォーマってで結果を返す
    - SPARQL endpointから返ってきたJSON-LDを、OASで定義されたフォーマットに応じてJSONに変換する手法
    - ユーザーが、POSTリクエストを通してKGに貢献するための、named graphに基づくメカニズム
    - KGに対するAPIの検証テストを自動生成

## (3) Why was it done that way (context within the field)?
- OBAは以下を実現するが、そういうものは過去にはない。
    - KGの内容の概要を、Web開発者にとっても理解しやすい一般的な形式(OAS)で提供（[W3C Linked Platform](http://www.w3.org/TR/2015/REC-ldp-20150226/)とその実装([Apache Marmotta](http://marmotta.apache.org/), [TrellisLDP](https://www.trellisldp.org/about.html))、[Linked Data Templates](https://atomgraph.github.io/Linked-Data-Templates/)は、Web開発者に分かる形でKGの内容の概要を提供しない）
    - ポストされるリソースはOpenAPIスキーマでvalidateされる。APIは、自動でオントロジーから生成。全ての結果は、生成されるOASに応じて、JSONで返される。（Basil, [GRLC](https://doi.org/10.1007/978-3-319-47602-5_48), [r4r](https://github.com/oeg-upm/r4r), [RAMOSE](https://github.com/opencitations/ramose)は、KGへのアクセスを簡単にするために、SPARQLクエリからREST APIを作成するが、POSTされたデータのValidationが必要だし、手動でのクエリ定義が必要で、JSON形式への変換も必要）
    - KG内のデータをクエリするために使用される、基礎となるオントロジーに精通している必要がない（[SPARQL transformer](https://doi.org/10.1007/978-3-030-30796-7_28), [SPARQL-JSONLD](https://github.com/usc-isi-i2/sparql-jsonld)、\[14\]は、Web開発者がKG内のデータをクエリするために使用される、基礎となるオントロジーに精通している必要がある）
    - OBAはAPIサーバを構築するための実装を提供（[owl2oas](https://github.com/hammar/owl2oas)はサーバ構築は未提供）
    - オントロジーを、KGの「内容」をexploitするためにAPIを生成するためのtemplateとして、ontologyを使っている。（[\[4\]](https://doi.org/10.5220/0005987201500157) は、オントロジーの「クラス」や「プロパティ」へアクセスするREST APIを定義）

## (4) What do the results show (figures and data tables)?
- Performance Analyses
    1. 結果をJSONに変換する際の、OBAによるオーバーヘッド　→　barely noticeable
    1. 毎秒の多重リクエスト応答のためのAPIの性能
        - reverse proxy cachingが有効であれば、60 queries/sec を200ms以下の遅延で制御可能。
        - cache無しの場合、10 queries/sec 以上でパフォーマンスが低下。使用するサーバの構成で改善可能かもしれない。

## (5) How did the author(s) interpret the results (interpretation/discussion)?
- Usage Examples: 三つの事例で、フレームワークの各要素をデモンストレーション。ベストプラクティスな手法である。

## (6) What should be done next? (Regarding this last question, the author(s) may provide some suggestions in the discussion, but the key is to ask yourself what you think should come next.)
- 以下は投稿時点で対応作業中
    - OWLとOAS間のmappingにおいて、複雑なaxiomatizationへの対応
        - propertyのrangeにunionとintersectionが同時に出てくる場合など
    - JSON-LDリクエストへの対応
- GraphQLへの追加対応も検討中
- 最も一般的なデータパターンでAPIを公開するために、オントロジーを既存のKGパターンマイニングツールと組み合わせる

## 読んだ範囲
斜め読み程度
