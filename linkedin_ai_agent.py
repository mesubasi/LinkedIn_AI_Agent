from PyPDF2 import PdfReader
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("BROWSER_DRIVER_PATH")
cv = os.getenv("CV_PATH")

reader = PdfReader(cv)
number_of_pages = len(reader.pages)
text = ''.join([reader.pages[i].extract_text() for i in range(number_of_pages)])

browser = Browser(
    config=BrowserConfig(
        chrome_instance_path=f"{path}",
    )
)

initial_actions = [
	{'open_tab': {'url': 'https://www.linkedin.com/feed/'}},
]

async def main():
    agent = Agent(
        task=f"""Go to LinkedIn.Once logged in, go to the ‘İş ilanları’ tab. Search for ‘Software Developer’ job postings in Istanbul.
                 On the left panel, go through the job postings one by one. Click on each job listing to review the details.
                 Analyze the job description and compare it with the provided CV: {text}. If the job requirements closely match the CV, mark it as ‘✅’ and proceed with the application. If the job does not align with the CV, mark it as ‘❌’ and skip to the next job posting.
                 If a job is marked as ‘✅’, click on the ‘Kolay Başvuru’ button and proceed with the application. Answer any required questions based on the job listing, including multiple-choice dropdowns, short answers, and yes/no questions.
                 Always click ‘Next’ to continue the application process until the final step. If a ‘Submit Application’ button appears at the end, click it to finalize the application.
                 If the application is successfully submitted, move on to the next job listing and repeat the same steps. However, if clicking the apply button redirects to an external website, do not proceed with the application. Instead, move to the next job posting in the list.""",
        llm=ChatOpenAI(model="gpt-4o"),
        browser=browser,
        initial_actions=initial_actions,
        save_conversation_path="logs/conversation"
    )

    result = await agent.run(max_steps=1000)
    input('Press Enter to close the browser...')
    await browser.close()
    print(result)
    
if __name__ == '__main__':
    asyncio.run(main())