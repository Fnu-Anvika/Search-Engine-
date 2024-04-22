#    CS-429 INFORMATION RETRIVAL

#### NAME: FNU ANVIKA
#### CWID : A20556800

## "A SEARCH ENGINE"

*This README document outlines the structure and execution instructions for the project which is mainly divided into 3 main parts*
  
###  - *Content Crawling*
###  - *Search indexing*
### - *Query processing* 

## Abstract:

This project intends to develop a web document crawler, indexer, and query processor using Scrapy, Scikit-Learn, and Flask, accordingly. The major purpose is to construct a complete system for online content retrieval, indexing, and querying. The crawler obtains web content in HTML format, the indexer generates an inverted index using TF-IDF representation and cosine similarity, and the query processor processes free text queries and delivers top-ranked results. 

### *Development Summary:*

The project involves the development of three main components: a web crawler, indexer, and query processor. The crawler initializes with a seed URL/domain and downloads web documents up to specified limits of maximum pages and depth. The indexer constructs an inverted index in pickle format using TF-IDF representation and cosine similarity scoring. The query processor handles free text queries in JSON format, performs query validation/error-checking, and returns top-ranked results based on the indexed content.

### *Objectives:*

  - Build a web crawler using Scrapy to retrieve HTML-formatted online pages.
  - Utilizing TF-IDF representation, construct an indexer usingScikit-Learn to produce an inverted index.
  - Use cosine similarity to index documents in a logical order.
  - Create a Flask-based query processor to handle free text inquiries and return the most relevant information.
  - To increase the accuracy of query processing, provide error-checking and query validation techniques.


 ### *Next Steps:*

- The web crawler should be enhanced and adjusted for more flexibility and performance.
-  To handle larger datasets and accelerate indexing, update the indexer.
- Include advanced search features like faceted search, wildcard search, and phrase search.
- Provide an intuitive user interface so that interacting with the query processor is a breeze.
- To ensure the accuracy and dependability of the system, do extensive testing and validation.


## Overview:

 ### *Soulution Outline*:

The three primary parts of the suggested system are a web crawler, an indexer, and a query processor. Together, they form an online search engine. As stated in the background material given, this approach is intended to tackle the difficulties involved in developing a search engine specifically targeted at personal blogs.

- The popular Python web scraping framework Scrapy library serves as the foundation for the web crawler component. The crawler is in charge of obtaining HTML web documents by following links to a predetermined maximum depth or number of pages, beginning with a set of seed URLs or domains. This makes it possible for the system to compile the material that needs to be indexed and made searchable.

- The indexer component builds an inverted index from the downloaded web content using the Scikit-Learn library, a popular Python machine learning tool. Words and the documents in which they occur are mapped by the inverted index, a data structure that also includes extra information like term frequency-inverse document frequency (TF-IDF) ratings. This makes it possible to efficiently retrieve relevant documents in response to user requests.

- The Flask web framework, a well-liked Python-based online application framework, is used to construct the query processor component. This part is in charge of receiving user queries, analyzing and verifying them, and delivering the top-k results that are sorted according to cosine similarity and the inverted index.

 ### *Literature*

The literature currently available on web crawlers and search engine architectures serves as an inspiration for the suggested solution. Because Scrapy offers a stable and expandable framework for online scraping operations, its use for web crawling has been extensively documented in the literature[1]. In information retrieval and search engine design, creating an inverted index using Scikit-Learn is a typical method. These elements may be integrated into a full search engine system in a manner similar to the design outlined in the blog article "Building a Search Engine"[2].

 ### *Proposed System*

To solve the issues of the collapsing blogosphere, the suggested system's primary characteristics are as follows:

- Focused crawling on personal blog sites that have been authorized in advance.
- Effective online content indexing and retrieval with TF-IDF-based ranking and an inverted index.
- An easy-to-use Flask-built query processing interface that lets users search the indexed material.

## Design 
   
### *System capabilities*

Three essential components make up the suggested solution:

- **Web Crawler**: Utilizing Scrapy, this part is responsible for locating and obtaining HTML-formatted online material.
   - It monitors links to a predetermined maximum depth or page count, starting with a set of seed URLs or domains.
   - It provides scalable and effective web crawling features.

- **Indexer** : Using the webpages the crawler downloaded, this Scikit-Learn program generates an inverted index.
   - The search results are ranked using the TF-IDF scores that are calculated for each phrase that is discovered in the documents.
   - For easy access, the inverted index is kept in a pickle file.

- **Query Processor**: This Flask-developed component offers a user-friendly interface for handling search queries.
   - It ensures proper input format and mistake correction by validating and processing user queries.
   - Using cosine similarity computations, it extracts the top-k ranked results from the inverted index.
   - It gives the user an easy-to-understand presentation of the search results.

### *Interactions*

These elements interact in the following ways:

- Using the supplied seed URLs or domains, the web crawler starts by retrieving web pages from authorized personal blog sites.
- After processing the downloaded web pages, the indexer creates an inverted index and saves the content's TF-IDF representation.
- The query processor receives a user-inputted search query, verifies the information, pulls pertinent articles from the inverted index, and ranks the results according to cosine similarity.
- The user is then shown the top k search results by the query processor.

### *Integration*

Together, these elements make up the search engine's structure. The material for indexing is provided by the crawler, user input and result display are handled by the query processor, and the indexer builds the data structures required for effective retrieval. By using well-known tools and frameworks like as Scikit-Learn, Flask, and Scrapy, the suggested system may be constructed in a scalable and modular manner, facilitating future upgrades and alterations with ease.


## Architecture - Software Components, Interfaces, Implementation

 ### *Scrapy-based Web Crawler:*

   - **Components**:

     - Scrapy Spider: in charge of obtaining HTML material, following links, and crawling webpages.
     - URL Manager: Oversees the crawling queue of URLs, imposing limitations on the maximum number of pages, maximum depth, and seed URL/domain.
     - HTML Downloader: This tool downloads web pages' HTML content.

   - **Interfaces:**
     - Input: max pages = 100, max depth = 2, and seed URL/domain.
     - Output: Web page HTML content downloaded.
     - The crawler-to-indexer interface makes it easier for downloaded web content to be sent from the crawler to the indexer.
     - Describes the formats and techniques for transferring document data.

   - **Implementation**:
     - Uses the Scrapy framework to enable scalable and effective web crawling.
     - Uses unique URL Manager and Scrapy Spider components to manage the crawling procedure.
     - Makes use of Scrapy's integrated link extraction and HTML downloader features.

    The seed URL/domain is "https://subslikescript.com/movies"


### *Indexer (based on Scikit-Learn):*

   - **Components.** 

     - Document Processor: It extracts text from the received HTML material and gets it ready for indexing.
     - Indexer: Creates the inverted index, determines the scores for TF-IDF, and saves the index in a pickle file.
     - Similarity Calculator: Determines the cosine similarity between search phrases and documents that have been indexed.

   - **Interfaces:**
     - Input: HTML material that was downloaded by the web crawler.
     - Output: A pickle-formatted inverted index.
     - Interface between the Processor and Indexer: - Permits the Indexer to transmit indexed data and query results to the Processor.

   - **Implementation**:

     -  The indexer uses Scikit-Learn to implement TF-IDF vectorization and compute cosine similarity.
     - The inverted index is displayed in the terminal in pickle format for quick access.
     - Pickle files the inverted index for quick retrieval during query processing.
     - The inverted index is displayed in the terminal in pickle format for quick access.
     - Additionally, the shapes of the Query vector and Cosine similarity are computed.

### *Flask-based Query Processor:*
   - **Components:** 

     - Query Parser: manages input formatting and error-checking while validating and processing user requests.
     - Retriever: Using cosine similarity, retrieves the top k results from the inverted index.
     - Result Formatter: Provides the user with a clear and straightforward presentation of the search results.

   - **Interfaces:**
      
      - Input: JSON-formatted user requests.
     - Output: A JSON format containing the top k search results.
     - The processor Specifies the format that must be used for the query parameters in order to provide ranked results.

   - **Implementation:**

     - Constructs a web application using Flask to process user requests.
     - Combines the Indexer component with search results retrieval and ranking.
     - Flask is used to manage query queries and develop RESTful API endpoints.
     - Cosine similarity scores are implemented for result ordering and query validation/error-checking is performed.
     - JSON-formatted requests are parsed and evaluated before returning suitable responses.
     - Ultimately, the cosine similarity score, author name, text, and tags for the entered query are returned.

The whole system architecture is modular in nature, with the crawler, indexer, and query processor the three main components each encapsulating its own functions and interacting with the others via well defined interfaces. This makes it possible for the system to be tested, maintained, and maybe extended in the future.

## Operation - Software Commands, Inputs, Installation

I have used Visual Studio code as my code Editor so as to run the following Commands.

##  *Software Commands:*

Crawler:
 -     scrapy crawl transcripts     
Initiates the web crawling process using the specified spider.

Indexer:
 -     python My_Indexer.py
  Executes the indexer script to construct the inverted index.

Processor:
 -     python My_Processor.py 
Runs the Flask-based processor for handling text queries.

### *Inputs:*

 Crawler:
 - `Seed URL/Domain = "https://subslikescript.com/movies":`The starting point for web crawling.
      
 - `Max Pages = 100:`The maximum number of web pages to crawl.
-  `Max Depth = 2:`The maximum depth of traversal for crawling.

 Indexer:
 - `HTML content downloaded by the crawler =`  `"all_pages.html"`

 Processor:
 - `JSON-formatted text queries for processing = "output.json"`.

###  *Installation:*

Crawler Setup:

 - Install Scrapy: `pip install scrapy`
 - Create Scrapy project: `scrapy startproject Crawler`
 - Define spiders and settings as per project requirements.

Indexer Setup:
 - Install Scikit-Learn: `pip install scikit-learn`
 - Implement Indexer script to process HTML content and construct the inverted index.

Processor Setup:
 - Install Flask: `pip install Flask`
 - Develop Flask-based processor for query handling and result presentation.

Integration:
Ensure proper integration among the crawler, indexer, and processor components.

Execution:
Run the respective scripts or Flask application to execute the functionalities.

## Conclusion - Success/Failure Results, Outputs, Caveats/Cautions

#### *Web Crawler Based on Scrapy*: 
   -  Success: Starting with the provided seed URL/domain, the crawler properly retrieves web content in HTML format while adhering to the specified maximum pages and depth.
   - Failure: The crawler may encounter issues, such as network outages, URL redirections, or inaccessible web pages, that prohibit it from fully or partially crawling the target domain.
   - Outputs: The HTML content that the crawler gathered from the websites is sent to the Indexer component.
   - Cautions/Warnings: The crawler should be designed to handle edge cases gently, such as respecting robots.txt, retrying failed searches, and abstaining from flooding the target page.

#### *An Indexer Based on Scikit-Learn:*
   - Success: After calculating the TF-IDF scores and creating an inverted index from the downloaded HTML content, the indexer stores the result in a pickle file.
   - Failure: Inaccurate or inadequate indexing might arise from the indexer's issues with text extraction, document processing, or index building.
   - Outputs: The inverted index that the indexer created and stored in a pickle file format is used by the Query Processor component.
   - Cautions/Warnings: Large-scale indexing should be considered when building the indexer, taking into consideration factors like memory use, disk space, and indexing performance.

#### *Query Processor Based on Flask:*
   - Success: The query processor presents the results in a JSON format after input validation and the retrieval of the top-k ranked results from the inverted index. It also does a good job of handling user requests.
   - Failure: The query processor's incapacity to understand the question, obtain results, or format the data may result in inaccurate or incomplete answers.
   - Results: The query processor provides the user with a JSON-formatted output that includes the top-k ranked search results.
   - Warnings/Cautions: When designing a query processor, consideration should be given to response speed, error correction, and scalability to manage a large volume of user queries.


## Data Sources 

## *Links, Downloads, Access Information:*
- https://youtu.be/m_3gjHGxIJc?si=F4v2tKm7kzhbyBXN
   
   This was the you-tube channel which I refered to so as to get the insights of web crawler using scrapy. Later then implemented on the other websites.

- https://subslikescript.com/movies
   
   The website which I have used in.

- https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/?couponCode=LETSLEARNNOWPP

   I have also taken into consideration of the Udemy course for the web crawling thing so as to know how the real world implementation is done.

- And for the second part, for calculating the inverted index and cosine similarity I have used the AI tools like, Chat-gpt, and Perplexity.

- And for the third part, that is flask. I stated to learn from a popular website, that is

 https://www.geeksforgeeks.org/flask-tutorial/

- The You-Tube channel which i referred was of, 

 https://youtu.be/Z1RJmh_OqeA?si=fOcslbdAm7gx-eqI

## Test Cases 

### *Framework, Harness, Coverage*

   - Web Crawler: Adherence to pre-set boundaries (such as seed URL/domain, maximum pages, maximum depth), successful execution of crawling, and management of special cases (like robots.txt, network disruptions, URL redirection).

   - Indexer: Precise calculations of cosine similarity, correct TF-IDF scoring, and successful indexing across diverse document formats.

   - Query Processor: Proper JSON structuring, validation of input, retrieval of the top-k outcomes, and successful processing of queries.

# Source Code 

### *Listings, Documentation, Dependencies (Open-Source)*

*My_Crawler:*

This code acts as a web crawling Scrapy spider. What it does is broken down as follows:

- It imports the required modules from Scrapy: `CloseSpider` to stop the spider when certain circumstances are fulfilled, `LinkExtractor` to extract links, and `CrawlSpider` and `Rule` to create a spider.

- A class called `TranscriptsSpider` is defined, which is an inheritor of `CrawlSpider`. The primary spider that will carry out the crawling is this class.

- This spider's unique identification is the `name` attribute.

- A list of domains that the spider is permitted to crawl may be found in the `allowed_domains` parameter.

 - A list of URLs from which the spider will begin its crawl is included in the `start_urls` property.

- The number of pages and depth the spider will crawl are limited by the `max_pages` and `max_depth` properties, respectively.

- The number of pages crawled is tracked using the `count` property.

- A tuple of one or more `Rule` objects makes up the `rules` attribute. Every `Rule` specifies an action that the spider must do. In this instance, the rule instructs the spider to call the `parse_item} method for each link and retrieve links from items that meet the XPath phrase.

- For every link that the rules extract, the `parse_item` function is invoked. It raises a `CloseSpider` exception to halt the spider after first determining whether the maximum depth or number of pages has been achieved. The current page's HTML content is then appended to a file called "all_pages.html." Ultimately, it uses XPath expressions to extract the data from the page and outputs it as a dictionary.

To put it simply, this spider begins at a specified URL, crawls the website via links, then retrieves and stores certain data from each page. When it reaches a particular depth or crawls a certain amount of pages, it stops. After data extraction, it may be processed or saved for later use. This is a typical web crawling and data extraction strategy.

### *My_Indexer*

In this Python script, you can run **cosine similarity** based search queries on a series of documents by creating a **inverted index** for them. This is how the code is broken down:

- **Importing Necessary Libraries**: First, the script imports the required libraries. Python object structures may be serialized and de-serialized with `pickle`. Text feature extraction is done using `CountVectorizer` and `TfidfTransformer` from `sklearn.feature_extraction.text`. Cosine similarity between vectors is computed using `cosine_similarity` from `sklearn.metrics.pairwise`.`bs4` `BeautifulSoup` is used to parse XML and HTML texts.

- **The Indexer Class** : `Indexer` is a class developed with methods to compute cosine similarity for a given query, save and load the index to/from a pickle file, and create an inverted index from a group of documents.

  - `__init__`: This is the `Indexer` class's constructor function. The `filename` is initialized, the documents are retrieved from the file, a term-document matrix is created using `CountVectorizer`, a tf-idf matrix is transformed using `TfidfTransformer}, and an inverted index is constructed.

  - `retrieve_documents`: This process extracts the text from the `<body>` tags after reading the HTML content from the file and parsing it using `BeautifulSoup`. The text is subsequently added to the `documents` list.

  - `build_inverted_index Technique`: This process generates the inverted index. It determines if each phrase appears in the document for each one. If so, the document's index is added to the posting list for the phrase in the inverted index.

  - `save_index_to_pickle`: This technique uses `pickle` to serialize the inverted index before writing it to a file.

  - `load_index_from_pickle`: This function uses `pickle` to de-serialize the serialized inverted index that it receives from a file.

  - `cosine_similarity`: The cosine similarity between a query and the documents is determined using this approach. After converting the question into a vector and figuring out how close the query vector and the tf-idf matrix are to each other, it provides the pages that have a cosine similarity score higher than 0.

The script shows you how to use the `Indexer` class. An instance of the `Indexer` class is created, the inverted index is saved to a pickle file, the index is loaded from the pickle file, and a cosine similarity search using a query entered by the user is carried out.

### *My_Processor*

This Python script utilizes Flask to build a web application for retrieving documents based on cosine similarity. Here is a breakdown of the code.

- **Importing Required Libraries**: The script starts by importing the essential libraries. `Flask`,`request`, `jsonify`, and `render_template` are utilized to develop the web application. The `CountVectorizer` and `TfidfTransformer` from `sklearn.feature_extraction.text` are used to extract text features. The `cosine_similarity` function from `sklearn.metrics.pairwise` is used to compute the cosine similarity between vectors. `json` is used to parse JSON data.

- **The Indexer Class**: The `Indexer` class has methods for creating a tf-idf matrix from a collection of documents and performing cosine similarity-based search queries.

    -  `__init__` This is the `Indexer` class's constructor. It initializes the `documents`, generates a term-document matrix with `CountVectorizer`, and converts the term-document matrix to a tf-idf matrix with `TfidfTransformer`.

    - `search' Method`: This method determines the cosine similarity between a query and the documents. It converts the query into a vector, computes the cosine similarity between the query vector and the tf-idf matrix, and delivers the top K documents with a cosine similarity score larger than zero.

- **Loading documents from the JSON file**: The `load_documents_from_json` method reads a JSON file, parses it, and extracts text from each element. The text content is then added to the `documents` list.

- **Initializing the Indexer**: The script then creates an instance of the `Indexer` class and loads the documents from the JSON file.

- **Create the Flask Application** The script generates a Flask app with two routes:

    - `/` Route: This route generates a search page using an HTML template.

    - `/search` route: This route accepts POST requests. It receives the query from the request data, searches using the 'Indexer', and delivers the search results in JSON format. If the query parameter is missing from the request data, it generates an error message. If no matching documents are identified, it displays a notice saying that no matching goods were discovered.

- **Running the Flask Application**: Finally, the script launches the Flask application in debugging mode.

# Bibiolgraphy

[1] Scikit-Learn Documentation. https://scikit-learn.org/stable/

[2] Building a Search Engine pt 1: The Crawler and Indexer. https://johnpatrickbender.com/projects/building_a_search_engine_pt_1.html

[3]  Web Crawler (Scrapy-based): https://github.com/scrapy/scrapy

[4] Indexer (Scikit-Learn based): https://github.com/scikit-learn/scikit-learn

[5] Query Processor (Flask-based): https://github.com/pallets/flask

[6] Scrapy Documentation: https://docs.scrapy.org/en/latest/

[7] Scikit-Learn Documentation: https://scikit-learn.org/stable/

[8] Flask Documentation: https://flask.palletsprojects.com/en/2.2.x/

[9] Scrapy: https://github.com/scrapy/scrapy

[10] Scikit-Learn: https://github.com/scikit-learn/scikit-learn

[11] Flask: https://github.com/pallets/flask

