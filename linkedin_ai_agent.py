from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
mail = os.getenv("LINKEDIN_EMAIL")
password = os.getenv("LINKEDIN_PASSWORD")
path = os.getenv("CHROME_DRIVER_PATH")

browser = Browser(
    config=BrowserConfig(
        chrome_instance_path=f"{path}",  # Path to Chrome executable

    )
)

async def main():
    agent = Agent(
        task=f"Go to LinkedIn. If the account is not open, scroll down to 'Sign in'. Log in with email: {mail} and password: {password}. "
             "Wait for the 2FA to pass. Once logged in, go to the 'Jobs' tab. Search for 'Software Developer' job postings in Istanbul. "
             "On the left panel, go through the job postings one by one. Click on each job listing to review the details. If the job posting has an ‘Easy Apply’ button, click on it and proceed with the application. "
             "During the application process, always click 'Next' until you reach the final step. If the application is successfully submitted, move on to the next job listing and repeat the same steps. "
             "However, if clicking the apply button redirects to an external website, do not proceed with the application. Instead, move to the next job posting in the list.",
        llm=ChatOpenAI(model="gpt-4o"),
        browser=browser,
    )
    result = await agent.run()

    input('Press Enter to close the browser...')
    await browser.close()
    print(result)
    

if __name__ == '__main__':
    asyncio.run(main())