What are Azure AI services?
===========================

-   Article
-   07/18/2023
-   1 contributor

Feedback

In this article
---------------

1.  [Available Azure AI services](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#available-azure-ai-services)
2.  [Pricing tiers and billing](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#pricing-tiers-and-billing)
3.  [Use Azure AI services in different development environments](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#use-azure-ai-services-in-different-development-environments)
4.  [Regional availability](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#regional-availability)

Show 5 more

Azure AI services help developers and organizations rapidly create intelligent, cutting-edge, market-ready, and responsible applications with out-of-the-box and pre-built and customizable APIs and models. Example applications include natural language processing for conversations, search, monitoring, translation, speech, vision, and decision-making.

 Note

As of July 2023, Azure AI services encompass all of what were previously known as Cognitive Services and Azure Applied AI Services. There are no changes to pricing. The names *Cognitive Services* and *Azure Applied AI* continue to be used in Azure billing, cost analysis, price list, and price APIs. There are no breaking changes to application programming interfaces (APIs) or SDKs.

Most Azure AI services are available through REST APIs and client library SDKs in popular development languages. For more information, see each service's documentation.

[](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#available-azure-ai-services)

Available Azure AI services
---------------------------

Select a service from the table below and learn how it can help you meet your development goals.

| Service | Description |
| --- | --- |
| ![Anomaly Detector icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/anomaly-detector.svg) [Anomaly Detector](https://learn.microsoft.com/en-us/azure/ai-services/anomaly-detector/) | Identify potential problems early on |
| ![Azure Cognitive Search icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/cognitive-search.svg) [Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/) | Bring AI-powered cloud search to your mobile and web apps |
| ![Azure OpenAI Service icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/azure.svg) [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/) | Perform a wide variety of natural language tasks |
| ![Bot service icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/bot-services.svg) [Bot Service](https://learn.microsoft.com/en-us/composer/) | Create bots and connect them across channels |
| ![Content Moderator icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/content-moderator.svg) [Content Moderator](https://learn.microsoft.com/en-us/azure/ai-services/content-moderator/) (retired) | Detect potentially offensive or unwanted content |
| ![Content Safety icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/content-safety.svg) [Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/) | An AI service that detects unwanted contents |
| ![Custom Vision icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/custom-vision.svg) [Custom Vision](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/) | Customize image recognition to fit your business |
| ![Document Intelligence icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/document-intelligence.svg) [Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/) | Turn documents into usable data at a fraction of the time and cost |
| ![Face icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/face.svg) [Face](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-identity) | Detect and identify people and emotions in images |
| ![Immersive Reader icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/immersive-reader.svg) [Immersive Reader](https://learn.microsoft.com/en-us/azure/ai-services/immersive-reader/) | Help users read and comprehend text |
| ![Language icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/language.svg) [Language](https://learn.microsoft.com/en-us/azure/ai-services/language-service/) | Build apps with industry-leading natural language understanding capabilities |
| ![Language Understanding icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/luis.svg) [Language understanding](https://learn.microsoft.com/en-us/azure/ai-services/luis/) (retired) | Understand natural language in your apps |
| ![Metrics Advisor icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/metrics-advisor.svg) [Metrics Advisor](https://learn.microsoft.com/en-us/azure/ai-services/metrics-advisor/) | An AI service that detects unwanted contents |
| ![Personalizer icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/personalizer.svg) [Personalizer](https://learn.microsoft.com/en-us/azure/ai-services/personalizer/) | Create rich, personalized experiences for each user |
| ![QnA Maker icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/luis.svg) [QnA maker](https://learn.microsoft.com/en-us/azure/ai-services/qnamaker/) (retired) | Distill information into easy-to-navigate questions and answers |
| ![Speech icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/speech.svg) [Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/) | Speech to text, text to speech, translation and speaker recognition |
| ![Translator icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/translator.svg) [Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/) | Translate more than 100 languages and dialects |
| ![Video Indexer icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/video-indexer.svg) [Video Indexer](https://learn.microsoft.com/en-us/azure/azure-video-indexer/) | Extract actionable insights from your videos |
| ![Vision icon](https://learn.microsoft.com/en-us/azure/ai-services/media/service-icons/vision.svg) [Vision](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/) | Analyze content in images and videos |

[](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#pricing-tiers-and-billing)

Pricing tiers and billing
-------------------------

Pricing tiers (and the amount you get billed) are based on the number of transactions you send using your authentication information. Each pricing tier specifies the:

-   maximum number of allowed transactions per second (TPS).
-   service features enabled within the pricing tier.
-   cost for a predefined number of transactions. Going above this number will cause an extra charge as specified in the [pricing details](https://azure.microsoft.com/pricing/details/cognitive-services/) for your service.

 Note

Many of the Azure AI services have a free tier you can use to try the service. To use the free tier, use `F0` as the SKU for your resource.

[](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#use-azure-ai-services-in-different-development-environments)

Use Azure AI services in different development environments
-----------------------------------------------------------

With Azure and Azure AI services, you have access to several development options, such as:

-   Automation and integration tools like Logic Apps and Power Automate.
-   Deployment options such as Azure Functions and the App Service.
-   Azure AI services Docker containers for secure access.
-   Tools like Apache Spark, Azure Databricks, Azure Synapse Analytics, and Azure Kubernetes Service for big data scenarios.

To learn more, see [Azure AI services development options](https://learn.microsoft.com/en-us/azure/ai-services/cognitive-services-development-options).

[](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#containers-for-azure-ai-services)

### Containers for Azure AI services

Azure AI services also provides several Docker containers that let you use the same APIs that are available from Azure, on-premises. These containers give you the flexibility to bring Azure AI services closer to your data for compliance, security, or other operational reasons. For more information, see [Azure AI containers](https://learn.microsoft.com/en-us/azure/ai-services/cognitive-services-container-support "Azure AI containers").

[](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#regional-availability)

Regional availability
---------------------

The APIs in Azure AI services are hosted on a growing network of Microsoft-managed data centers. You can find the regional availability for each API in [Azure region list](https://azure.microsoft.com/regions "Azure region list").

Looking for a region we don't support yet? Let us know by filing a feature request on our [UserVoice forum](https://feedback.azure.com/d365community/forum/09041fae-0b25-ec11-b6e6-000d3a4f0858).

[](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#language-support)

Language support
----------------

Azure AI services supports a wide range of cultural languages at the service level. You can find the language availability for each API in the [supported languages list](https://learn.microsoft.com/en-us/azure/ai-services/language-support "Supported languages list").

[](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#security)

Security
--------

Azure AI services provides a layered security model, including [authentication](https://learn.microsoft.com/en-us/azure/ai-services/authentication "Authentication") with Azure Active Directory credentials, a valid resource key, and [Azure Virtual Networks](https://learn.microsoft.com/en-us/azure/ai-services/cognitive-services-virtual-networks "Azure Virtual Networks").

[](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#certifications-and-compliance)

Certifications and compliance
-----------------------------

Azure AI services has been awarded certifications such as CSA STAR Certification, FedRAMP Moderate, and HIPAA BAA. You can [download](https://gallery.technet.microsoft.com/Overview-of-Azure-c1be3942 "Download") certifications for your own audits and security reviews.

To understand privacy and data management, go to the [Trust Center](https://servicetrust.microsoft.com/ "Trust Center").

[](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#help-and-support)

Help and support
----------------

Azure AI services provides several support options to help you move forward with creating intelligent applications. Azure AI services also has a strong community of developers that can help answer your specific questions. For a full list of support options available to you, see [Azure AI services support and help options](https://learn.microsoft.com/en-us/azure/ai-services/cognitive-services-support-options "Azure AI services support and help options").

[](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#next-steps)

Next steps
----------

-   Select a service from the tables above and learn how it can help you meet your development goals.
-   [Create a multi-service resource](https://learn.microsoft.com/en-us/azure/ai-services/multi-service-resource?pivots=azportal)
-   [Plan and manage costs for Azure AI services](https://learn.microsoft.com/en-us/azure/ai-services/plan-manage-costs)
