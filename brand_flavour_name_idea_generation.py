from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import secret_openai_key
import os
os.environ['OPENAI_API_KEY'] = secret_openai_key.openapi_key


llm = OpenAI(temperature=0.7)

def gen_name_catalog(sector):
    # chain 1: Name of business

    prompt_name_company =  PromptTemplate(
                            input_variables = ['sector'],
                            Template = "What should be a suitable name for a business in {sector}? Suggest one name.")
    
    name_chain = LLMChain(llm=llm, prompt=prompt_name_company, output_key="company_name")

    prompt_product_catalogue = PromptTemplate(
                                input_variables = ['company_name'],
                                Template = "can you name 10 products for the {company_name}. Return it as a comma separated string"
                                )

    catalog_gen_chain = LLMChain(llm=llm, prompt=prompt_product_catalogue, output_key="catalogue")

    chain = SequentialChain(
        chains=[name_chain, catalog_gen_chain],
        input_variables=['sector'],
        output_variables=['company_name', "catalogue"]
    )

    response = chain({'sector': sector})

    return response


if __name__ == "__main__":
    print(gen_name_catalog("beverage"))

