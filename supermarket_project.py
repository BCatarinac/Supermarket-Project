{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "711e3fba",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b7aafcdc",
   "metadata": {},
   "outputs": [],
   "source": [
    "path_to_csv = 'supermarket_sales.csv'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "04242078",
   "metadata": {},
   "outputs": [],
   "source": [
    "supermarket = pd.read_csv(path_to_csv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "63a65c5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "supermarket.columns = [column.lower().replace(\" \", \"_\") for column in supermarket.columns]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cf79afec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>invoice_id</th>\n",
       "      <th>branch</th>\n",
       "      <th>city</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>gender</th>\n",
       "      <th>product_line</th>\n",
       "      <th>unit_price</th>\n",
       "      <th>quantity</th>\n",
       "      <th>tax_5%</th>\n",
       "      <th>total</th>\n",
       "      <th>date</th>\n",
       "      <th>time</th>\n",
       "      <th>payment</th>\n",
       "      <th>cogs</th>\n",
       "      <th>gross_margin_percentage</th>\n",
       "      <th>gross_income</th>\n",
       "      <th>rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>750-67-8428</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Member</td>\n",
       "      <td>Female</td>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>74.69</td>\n",
       "      <td>7</td>\n",
       "      <td>26.1415</td>\n",
       "      <td>548.9715</td>\n",
       "      <td>1/5/2019</td>\n",
       "      <td>13:08</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>522.83</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>26.1415</td>\n",
       "      <td>9.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>226-31-3081</td>\n",
       "      <td>C</td>\n",
       "      <td>Naypyitaw</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Female</td>\n",
       "      <td>Electronic accessories</td>\n",
       "      <td>15.28</td>\n",
       "      <td>5</td>\n",
       "      <td>3.8200</td>\n",
       "      <td>80.2200</td>\n",
       "      <td>3/8/2019</td>\n",
       "      <td>10:29</td>\n",
       "      <td>Cash</td>\n",
       "      <td>76.40</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>3.8200</td>\n",
       "      <td>9.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>631-41-3108</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Male</td>\n",
       "      <td>Home and lifestyle</td>\n",
       "      <td>46.33</td>\n",
       "      <td>7</td>\n",
       "      <td>16.2155</td>\n",
       "      <td>340.5255</td>\n",
       "      <td>3/3/2019</td>\n",
       "      <td>13:23</td>\n",
       "      <td>Credit card</td>\n",
       "      <td>324.31</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>16.2155</td>\n",
       "      <td>7.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>123-19-1176</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Member</td>\n",
       "      <td>Male</td>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>58.22</td>\n",
       "      <td>8</td>\n",
       "      <td>23.2880</td>\n",
       "      <td>489.0480</td>\n",
       "      <td>1/27/2019</td>\n",
       "      <td>20:33</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>465.76</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>23.2880</td>\n",
       "      <td>8.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>373-73-7910</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Male</td>\n",
       "      <td>Sports and travel</td>\n",
       "      <td>86.31</td>\n",
       "      <td>7</td>\n",
       "      <td>30.2085</td>\n",
       "      <td>634.3785</td>\n",
       "      <td>2/8/2019</td>\n",
       "      <td>10:37</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>604.17</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>30.2085</td>\n",
       "      <td>5.3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    invoice_id branch       city customer_type  gender  \\\n",
       "0  750-67-8428      A     Yangon        Member  Female   \n",
       "1  226-31-3081      C  Naypyitaw        Normal  Female   \n",
       "2  631-41-3108      A     Yangon        Normal    Male   \n",
       "3  123-19-1176      A     Yangon        Member    Male   \n",
       "4  373-73-7910      A     Yangon        Normal    Male   \n",
       "\n",
       "             product_line  unit_price  quantity   tax_5%     total       date  \\\n",
       "0       Health and beauty       74.69         7  26.1415  548.9715   1/5/2019   \n",
       "1  Electronic accessories       15.28         5   3.8200   80.2200   3/8/2019   \n",
       "2      Home and lifestyle       46.33         7  16.2155  340.5255   3/3/2019   \n",
       "3       Health and beauty       58.22         8  23.2880  489.0480  1/27/2019   \n",
       "4       Sports and travel       86.31         7  30.2085  634.3785   2/8/2019   \n",
       "\n",
       "    time      payment    cogs  gross_margin_percentage  gross_income  rating  \n",
       "0  13:08      Ewallet  522.83                 4.761905       26.1415     9.1  \n",
       "1  10:29         Cash   76.40                 4.761905        3.8200     9.6  \n",
       "2  13:23  Credit card  324.31                 4.761905       16.2155     7.4  \n",
       "3  20:33      Ewallet  465.76                 4.761905       23.2880     8.4  \n",
       "4  10:37      Ewallet  604.17                 4.761905       30.2085     5.3  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "supermarket.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "830c3936",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "invoice_id                 1000\n",
       "branch                     1000\n",
       "city                       1000\n",
       "customer_type              1000\n",
       "gender                     1000\n",
       "product_line               1000\n",
       "unit_price                 1000\n",
       "quantity                   1000\n",
       "tax_5%                     1000\n",
       "total                      1000\n",
       "date                       1000\n",
       "time                       1000\n",
       "payment                    1000\n",
       "cogs                       1000\n",
       "gross_margin_percentage    1000\n",
       "gross_income               1000\n",
       "rating                     1000\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "supermarket.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "25556d88",
   "metadata": {},
   "outputs": [],
   "source": [
    "supermarket = supermarket.rename(columns={'branch': 'branch_name'})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f27e29f3",
   "metadata": {},
   "source": [
    "## TABLE INVOICE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6f394837",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice = supermarket [['invoice_id', 'date', 'time', 'quantity', 'total', 'payment','customer_type', 'product_line', 'branch_name', 'unit_price']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "dddaf31e",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice.to_csv('invoice.csv', index='customer_id')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d6489e19",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice = invoice.rename(columns={'Unnamed: 0': 'customer_id'})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a29faefb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "\n",
    "invoice['customer_id'] = range(len(invoice))\n",
    "\n",
    "invoice.set_index('customer_id', inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a3cad566",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>invoice_id</th>\n",
       "      <th>date</th>\n",
       "      <th>time</th>\n",
       "      <th>quantity</th>\n",
       "      <th>total</th>\n",
       "      <th>payment</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>product_line</th>\n",
       "      <th>branch_name</th>\n",
       "      <th>unit_price</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>customer_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>750-67-8428</td>\n",
       "      <td>1/5/2019</td>\n",
       "      <td>13:08</td>\n",
       "      <td>7</td>\n",
       "      <td>548.9715</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>Member</td>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>A</td>\n",
       "      <td>74.69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>226-31-3081</td>\n",
       "      <td>3/8/2019</td>\n",
       "      <td>10:29</td>\n",
       "      <td>5</td>\n",
       "      <td>80.2200</td>\n",
       "      <td>Cash</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Electronic accessories</td>\n",
       "      <td>C</td>\n",
       "      <td>15.28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>631-41-3108</td>\n",
       "      <td>3/3/2019</td>\n",
       "      <td>13:23</td>\n",
       "      <td>7</td>\n",
       "      <td>340.5255</td>\n",
       "      <td>Credit card</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Home and lifestyle</td>\n",
       "      <td>A</td>\n",
       "      <td>46.33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>123-19-1176</td>\n",
       "      <td>1/27/2019</td>\n",
       "      <td>20:33</td>\n",
       "      <td>8</td>\n",
       "      <td>489.0480</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>Member</td>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>A</td>\n",
       "      <td>58.22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>373-73-7910</td>\n",
       "      <td>2/8/2019</td>\n",
       "      <td>10:37</td>\n",
       "      <td>7</td>\n",
       "      <td>634.3785</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Sports and travel</td>\n",
       "      <td>A</td>\n",
       "      <td>86.31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>233-67-5758</td>\n",
       "      <td>1/29/2019</td>\n",
       "      <td>13:46</td>\n",
       "      <td>1</td>\n",
       "      <td>42.3675</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>C</td>\n",
       "      <td>40.35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>303-96-2227</td>\n",
       "      <td>3/2/2019</td>\n",
       "      <td>17:16</td>\n",
       "      <td>10</td>\n",
       "      <td>1022.4900</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Home and lifestyle</td>\n",
       "      <td>B</td>\n",
       "      <td>97.38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>727-02-1313</td>\n",
       "      <td>2/9/2019</td>\n",
       "      <td>13:22</td>\n",
       "      <td>1</td>\n",
       "      <td>33.4320</td>\n",
       "      <td>Cash</td>\n",
       "      <td>Member</td>\n",
       "      <td>Food and beverages</td>\n",
       "      <td>A</td>\n",
       "      <td>31.84</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>347-56-2442</td>\n",
       "      <td>2/22/2019</td>\n",
       "      <td>15:33</td>\n",
       "      <td>1</td>\n",
       "      <td>69.1110</td>\n",
       "      <td>Cash</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Home and lifestyle</td>\n",
       "      <td>A</td>\n",
       "      <td>65.82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>849-09-3807</td>\n",
       "      <td>2/18/2019</td>\n",
       "      <td>13:28</td>\n",
       "      <td>7</td>\n",
       "      <td>649.2990</td>\n",
       "      <td>Cash</td>\n",
       "      <td>Member</td>\n",
       "      <td>Fashion accessories</td>\n",
       "      <td>A</td>\n",
       "      <td>88.34</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "              invoice_id       date   time  quantity      total      payment  \\\n",
       "customer_id                                                                    \n",
       "0            750-67-8428   1/5/2019  13:08         7   548.9715      Ewallet   \n",
       "1            226-31-3081   3/8/2019  10:29         5    80.2200         Cash   \n",
       "2            631-41-3108   3/3/2019  13:23         7   340.5255  Credit card   \n",
       "3            123-19-1176  1/27/2019  20:33         8   489.0480      Ewallet   \n",
       "4            373-73-7910   2/8/2019  10:37         7   634.3785      Ewallet   \n",
       "...                  ...        ...    ...       ...        ...          ...   \n",
       "995          233-67-5758  1/29/2019  13:46         1    42.3675      Ewallet   \n",
       "996          303-96-2227   3/2/2019  17:16        10  1022.4900      Ewallet   \n",
       "997          727-02-1313   2/9/2019  13:22         1    33.4320         Cash   \n",
       "998          347-56-2442  2/22/2019  15:33         1    69.1110         Cash   \n",
       "999          849-09-3807  2/18/2019  13:28         7   649.2990         Cash   \n",
       "\n",
       "            customer_type            product_line branch_name  unit_price  \n",
       "customer_id                                                                \n",
       "0                  Member       Health and beauty           A       74.69  \n",
       "1                  Normal  Electronic accessories           C       15.28  \n",
       "2                  Normal      Home and lifestyle           A       46.33  \n",
       "3                  Member       Health and beauty           A       58.22  \n",
       "4                  Normal       Sports and travel           A       86.31  \n",
       "...                   ...                     ...         ...         ...  \n",
       "995                Normal       Health and beauty           C       40.35  \n",
       "996                Normal      Home and lifestyle           B       97.38  \n",
       "997                Member      Food and beverages           A       31.84  \n",
       "998                Normal      Home and lifestyle           A       65.82  \n",
       "999                Member     Fashion accessories           A       88.34  \n",
       "\n",
       "[1000 rows x 10 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "invoice"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1228a9b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice.to_csv('invoice.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2fabfb12",
   "metadata": {},
   "source": [
    "## INVOICE DETAILS "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c4c047b",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice_details = supermarket [['gross_margin_percentage','gross_income', 'cogs', 'unit_price', 'tax_5%','rating', 'invoice_id', 'product_line']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24ea78d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice_details"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57341150",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice_details.index.name = 'invoice_details_id'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85a1adfa",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice_details = invoice_details.rename(columns={'Unnamed: 0': 'invoice_details_id'})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "080d4f48",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice_details.to_csv('invoice_details.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff77c827",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice_details"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3e618b5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "a8f0180d",
   "metadata": {},
   "source": [
    "## TABELA BRANCH"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "746f4b0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "path_to_csv = 'branch.csv'\n",
    "\n",
    "branch = pd.read_csv(path_to_csv)\n",
    "branch.columns = [column.lower().replace(\" \", \"_\") for column in branch.columns]\n",
    "\n",
    "branch.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b57f74a",
   "metadata": {},
   "outputs": [],
   "source": [
    "branch = branch.rename(columns={'Unnamed: 0': 'branch_id', 'branch': 'branch_name'})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51a2b4f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "branch.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5db24514",
   "metadata": {},
   "outputs": [],
   "source": [
    "path_to_csv = 'branch.csv'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6e6c517",
   "metadata": {},
   "outputs": [],
   "source": [
    "branch.to_csv('branch.csv', index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "530d2a70",
   "metadata": {},
   "source": [
    "## TABLE CUSTOMER "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "011fb1f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "path_to_csv = 'customer.csv'\n",
    "\n",
    "customer = pd.read_csv(path_to_csv)\n",
    "customer.columns = [column.lower().replace(\" \", \"_\") for column in customer.columns]\n",
    "\n",
    "customer.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ff49dfa",
   "metadata": {},
   "outputs": [],
   "source": [
    "customer = customer.rename(columns={'unnamed:_0': 'customer_id'})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "365d9edf",
   "metadata": {},
   "outputs": [],
   "source": [
    "customer.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d0bb91b",
   "metadata": {},
   "outputs": [],
   "source": [
    "customer.to_csv('customer.csv', index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a75eaa6",
   "metadata": {},
   "source": [
    "## TABLE PRODUCTS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7dcd8e73",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "path_to_csv = 'products.csv'\n",
    "\n",
    "products = pd.read_csv(path_to_csv)\n",
    "products.columns = [column.lower().replace(\" \", \"_\") for column in products.columns]\n",
    "\n",
    "products.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cff1e0ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "products = products.rename(columns={'Unnamed: 0': 'product_id'})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c3fa681",
   "metadata": {},
   "outputs": [],
   "source": [
    "products.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f32d289",
   "metadata": {},
   "outputs": [],
   "source": [
    "products.to_csv('products.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48985b66",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eeb350da",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf8716ee",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "bb2ccfb0",
   "metadata": {},
   "source": [
    "## TABLE INVOICE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92a33e1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "path_to_csv = 'invoice.csv'\n",
    "\n",
    "invoice = pd.read_csv(path_to_csv)\n",
    "invoice.columns = [column.lower().replace(\" \", \"_\") for column in invoice.columns]\n",
    "\n",
    "invoice.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba4131d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice = invoice.rename(columns={'Unnamed: 0': 'Invoice_id'})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b13e17f",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5dc826dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice.to_csv('invoice.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4392611f",
   "metadata": {},
   "outputs": [],
   "source": [
    "invoice = invoice [['invoice_id', 'Date', 'Time', 'Quantity', 'Total', 'Payment']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e40c72e8",
   "metadata": {},
   "source": [
    "# PLOTS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "69c1da8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "path_to_csv2 = \"/Users/sergiopizzolante/Desktop/Ironhack/Week4/GroupProject/amount_per_gender.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8c82dfe4",
   "metadata": {},
   "outputs": [],
   "source": [
    "spending_per_gender = pd.read_csv(path_to_csv2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "30a5d47a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAJOCAYAAACqS2TfAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAABOCUlEQVR4nO3deXxNd+L/8ffNKomICEmEICq1NMTSVi1DlNgZTKutDlo62toagjJKlUosrdLG2jEYvqb6raUtnZKqtaolqK21NSpKGkuaCJGQnN8f/bq/3gkV1z1uEq/n43Eej5zPOffc971/iHc+Z7EYhmEIAAAAAAA4nIuzAwAAAAAAUFJRugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQD4HYvFUqhl8+bNtz1WXFyc1qxZc9d5JkyYcFfHuJcyMzM1ZcoUNW7cWGXLlpW7u7uCgoLUvn17LV++XDk5OU7JNWHCBFksFqe8NwDg/ubm7AAAABQlX3/9tc36pEmTtGnTJn355Zc243Xq1LntseLi4vTEE0+oW7dujoxYZB07dkzt27dXWlqaBgwYoLFjx8rf319nz57V+vXr1a9fP33//feaNGmSs6MCAHDPULoBAPidxx57zGa9QoUKcnFxKTB+P7p27ZosFovc3Ar+9+H69evq1q2bLl68qG+//Va1a9e22d6zZ0+NHz9ee/fuvVdxTXXlyhV5e3s7OwYAoBjg9HIAAO7QxYsXNXDgQFWqVEkeHh6qXr26xo4da3PqtMVi0eXLl7VkyRLrKelRUVGSpHPnzmngwIGqU6eOSpcurcDAQD3++OPatm2bXXlOnjwpi8WiadOmafLkyapSpYpKlSqlhx9+WBs3biyw/7Fjx9SrVy8FBgbK09NTtWvX1uzZs2322bx5sywWi5YuXarY2FhVqlRJnp6eOn78+E0zrF69WocPH9bYsWMLFO4bqlatWmDWPzMzUyNGjFBYWJg8PDxUqVIlxcTE6PLlyzb7WSwWDR48WEuXLlXt2rXl7e2tyMhIrV27tsD7rFu3TvXr15enp6fCwsL01ltv3TSPYRiaM2eO6tevLy8vL/n7++uJJ57Qjz/+aLNfVFSUIiIitHXrVjVt2lTe3t7q16/fTY8JAMB/Y6YbAIA7cPXqVbVq1UonTpzQG2+8oXr16mnbtm2Kj4/Xvn37tG7dOkm/nab++OOPq1WrVho3bpwkqUyZMpJ+K+2S9Prrrys4OFhZWVlavXq1oqKitHHjRms5v1MJCQmqWrWqZs6cqfz8fE2bNk0dOnTQli1b1KRJE0nS4cOH1bRpU1WpUkVvv/22goODtX79eg0dOlTnz5/X66+/bnPMMWPGqEmTJpo3b55cXFwUGBh40/dOTEyUJHXt2rXQea9cuaKWLVvq9OnT+vvf/6569erp0KFDGj9+vA4cOKAvvvjC5jrsdevWadeuXZo4caJKly6tadOmqXv37jpy5IiqV68uSdq4caP+/Oc/q0mTJvrggw+Ul5enadOm6Zdffinw/i+++KIWL16soUOHaurUqbp48aImTpyopk2b6rvvvlNQUJB137Nnz+qvf/2rRo0apbi4OLm4MG8BACgkAwAA3FLfvn0NHx8f6/q8efMMScaHH35os9/UqVMNScaGDRusYz4+Pkbfvn1v+x7Xr183rl27ZrRu3dro3r27zTZJxuuvv/6Hr09OTjYkGSEhIUZ2drZ1PDMz0yhXrpzRpk0b61i7du2MypUrGxkZGTbHGDx4sFGqVCnj4sWLhmEYxqZNmwxJRosWLW6b3zAMo3379oYk4+rVqzbj+fn5xrVr16zL9evXrdvi4+MNFxcXY9euXTav+eijjwxJxmeffWbzPQQFBRmZmZnWsdTUVMPFxcWIj4+3jjVu3PiW38Pv/9vz9ddfG5KMt99+2+a9U1JSDC8vL2PUqFHWsZYtWxqSjI0bNxbquwAA4Pf4My0AAHfgyy+/lI+Pj5544gmb8eeee06Sbno6983MmzdPDRs2VKlSpeTm5iZ3d3dt3LhR33//vd3ZevTooVKlSlnXfX191aVLF23dulV5eXm6evWqNm7cqO7du8vb21vXr1+3Lh07dtTVq1e1c+dOm2P+5S9/sTuPJM2aNUvu7u7WJTIy0rpt7dq1ioiIUP369W2ytGvX7qZ3iG/VqpV8fX2t60FBQQoMDNRPP/0kSbp8+bJ27dp1y+/h99auXSuLxaK//vWvNu8dHBysyMjIAu/t7++vxx9//K6+CwDA/YnSDQDAHbhw4YKCg4MLPH4qMDBQbm5uunDhwm2PMWPGDL388stq3LixVq5cqZ07d2rXrl1q3769srOz7c4WHBx807Hc3FxlZWXpwoULun79ut577z2bIuzu7q6OHTtKks6fP2/z+ooVKxbqvatUqSJJ1gJ8Q69evbRr1y7t2rVLDRs2tNn2yy+/aP/+/QWy+Pr6yjCMAlkCAgIKvK+np6f1O0tPT1d+fv4tv4f/fm/DMBQUFFTg/Xfu3Gn39wAAwH/jmm4AAO5AQECAvvnmGxmGYVO809LSdP36dZUvX/62x1i2bJmioqI0d+5cm/FLly7dVbbU1NSbjnl4eKh06dJyd3eXq6urevfurUGDBt30GGFhYTbrhX22dXR0tBYsWKBPPvlEI0aMsI4HBgZarwP39fW1udlc+fLl5eXlpX/+8583PWZhvsvf8/f3l8ViueX38N/Htlgs2rZtmzw9PQvs/99jPOMbAGAvSjcAAHegdevW+vDDD7VmzRp1797dOv6vf/3Luv2G38/C/p7FYilQ6vbv36+vv/5aoaGhdmdbtWqVpk+fbj21+tKlS/r000/1pz/9Sa6urvL29larVq20d+9e1atXTx4eHna/13/r3r276tSpo7i4OHXu3Fm1atW67Ws6d+6suLg4BQQEFCj79vDx8dGjjz56y+/hv997ypQp+vnnn9WzZ8+7fm8AAG6F0g0AwB3o06ePZs+erb59++rkyZOqW7eutm/frri4OHXs2FFt2rSx7lu3bl1t3rxZn376qSpWrChfX1/VrFlTnTt31qRJk/T666+rZcuWOnLkiCZOnKiwsDBdv37d7myurq6Kjo7W8OHDlZ+fr6lTpyozM1NvvPGGdZ9Zs2apefPm+tOf/qSXX35Z1apV06VLl3T8+HF9+umn+vLLL+1+7zVr1qhdu3Z69NFH9be//U1RUVHy9/fXr7/+qm+++UbfffedzePEYmJitHLlSrVo0ULDhg1TvXr1lJ+fr1OnTmnDhg2KjY1V48aN7yjHpEmT1L59e0VHRys2NlZ5eXmaOnWqfHx8rHeNl6RmzZppwIABev7557V79261aNFCPj4+Onv2rLZv3666devq5Zdftuu7AADg9yjdAADcgVKlSmnTpk0aO3aspk+frnPnzqlSpUoaMWJEgcdtzZo1S4MGDdLTTz9tfTzW5s2bNXbsWF25ckULFy7UtGnTVKdOHc2bN0+rV68ucAOvOzF48GBdvXpVQ4cOVVpamh566CGtW7dOzZo1s+5Tp04d7dmzR5MmTdJrr72mtLQ0lS1bVuHh4dbruu0VHh6uffv2afbs2Vq9erX+8Y9/6MqVKypXrpwiIyM1efJk6w3npN9mprdt26YpU6ZowYIFSk5OlpeXl6pUqaI2bdqoWrVqd5whOjpaa9as0WuvvaannnpKwcHBGjhwoLKzs23++CBJ8+fP12OPPab58+drzpw5ys/PV0hIiJo1a6ZHH330rr4LAABusBiGYTg7BAAAsN/JkycVFham6dOn21xPDQAAnI+7lwMAAAAAYBJKNwAAAAAAJuH0cgAAAAAATMJMNwAAAAAAJqF0AwAAAABgEko3AAAAAAAm4TndkvLz83XmzBn5+vrKYrE4Ow4AAAAAoIgzDEOXLl1SSEiIXFxuPZ9N6ZZ05swZhYaGOjsGAAAAAKCYSUlJUeXKlW+5ndItydfXV9JvX1aZMmWcnAYAAAAAUNRlZmYqNDTU2idvhdItWU8pL1OmDKUbAAAAAFBot7tEmRupAQAAAABgEko3AAAAAAAmoXQDAAAAAGASSjcAAAAAACahdAMAAAAAYBJKNwAAAAAAJqF0AwAAAABgEko3AAAAAAAmoXQDAAAAAGASSjcAAAAAACahdAMAAAAAYBJKNwAAAAAAJqF0AwAAAABgEko3AAAAAAAmoXQDAAAAAGASSjcAAAAAACahdAMAAAAAYBJKNwAAAAAAJqF0AwAAAABgEko3AAAAAAAmcXN2ANyBLbudnQAAcDdaPuzsBAAA4B5jphsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwiVNL99atW9WlSxeFhITIYrFozZo1Bfb5/vvv1bVrV/n5+cnX11ePPfaYTp06Zd2ek5OjIUOGqHz58vLx8VHXrl11+vTpe/gpAAAAAAC4OaeW7suXLysyMlIJCQk33X7ixAk1b95ctWrV0ubNm/Xdd99p3LhxKlWqlHWfmJgYrV69Wh988IG2b9+urKwsde7cWXl5effqYwAAAAAAcFMWwzAMZ4eQJIvFotWrV6tbt27Wsaefflru7u5aunTpTV+TkZGhChUqaOnSpXrqqackSWfOnFFoaKg+++wztWvXrlDvnZmZKT8/P2VkZKhMmTJ3/VlMs2W3sxMAAO5Gy4ednQAAADhIYXtkkb2mOz8/X+vWrdODDz6odu3aKTAwUI0bN7Y5BT0pKUnXrl1T27ZtrWMhISGKiIjQjh07bnnsnJwcZWZm2iwAAAAAADhakS3daWlpysrK0pQpU9S+fXtt2LBB3bt3V48ePbRlyxZJUmpqqjw8POTv72/z2qCgIKWmpt7y2PHx8fLz87MuoaGhpn4WAAAAAMD9qciW7vz8fEnSn//8Zw0bNkz169fX6NGj1blzZ82bN+8PX2sYhiwWyy23jxkzRhkZGdYlJSXFodkBAAAAAJCKcOkuX7683NzcVKdOHZvx2rVrW+9eHhwcrNzcXKWnp9vsk5aWpqCgoFse29PTU2XKlLFZAAAAAABwtCJbuj08PPTII4/oyJEjNuNHjx5V1apVJUmNGjWSu7u7EhMTrdvPnj2rgwcPqmnTpvc0LwAAAAAA/83NmW+elZWl48ePW9eTk5O1b98+lStXTlWqVNHIkSP11FNPqUWLFmrVqpU+//xzffrpp9q8ebMkyc/PT/3791dsbKwCAgJUrlw5jRgxQnXr1lWbNm2c9KkAAAAAAPiNU0v37t271apVK+v68OHDJUl9+/bV4sWL1b17d82bN0/x8fEaOnSoatasqZUrV6p58+bW17zzzjtyc3NTz549lZ2drdatW2vx4sVydXW9558HAAAAAIDfKzLP6XYmntMNALgneE43AAAlRrF/TjcAAAAAAMUdpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTOPU53QAAAGZZdeSssyMAAOzUo2ZFZ0dwGGa6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAkzi1dG/dulVdunRRSEiILBaL1qxZc8t9X3zxRVksFs2cOdNmPCcnR0OGDFH58uXl4+Ojrl276vTp0+YGBwAAAACgEJxaui9fvqzIyEglJCT84X5r1qzRN998o5CQkALbYmJitHr1an3wwQfavn27srKy1LlzZ+Xl5ZkVGwAAAACAQnFz5pt36NBBHTp0+MN9fv75Zw0ePFjr169Xp06dbLZlZGRo4cKFWrp0qdq0aSNJWrZsmUJDQ/XFF1+oXbt2pmUHAAAAAOB2ivQ13fn5+erdu7dGjhyphx56qMD2pKQkXbt2TW3btrWOhYSEKCIiQjt27LjlcXNycpSZmWmzAAAAAADgaEW6dE+dOlVubm4aOnToTbenpqbKw8ND/v7+NuNBQUFKTU295XHj4+Pl5+dnXUJDQx2aGwAAAAAAqQiX7qSkJM2aNUuLFy+WxWK5o9cahvGHrxkzZowyMjKsS0pKyt3GBQAAAACggCJburdt26a0tDRVqVJFbm5ucnNz008//aTY2FhVq1ZNkhQcHKzc3Fylp6fbvDYtLU1BQUG3PLanp6fKlCljswAAAAAA4GhFtnT37t1b+/fv1759+6xLSEiIRo4cqfXr10uSGjVqJHd3dyUmJlpfd/bsWR08eFBNmzZ1VnQAAAAAACQ5+e7lWVlZOn78uHU9OTlZ+/btU7ly5VSlShUFBATY7O/u7q7g4GDVrFlTkuTn56f+/fsrNjZWAQEBKleunEaMGKG6deta72YOAAAAAICzOLV07969W61atbKuDx8+XJLUt29fLV68uFDHeOedd+Tm5qaePXsqOztbrVu31uLFi+Xq6mpGZAAAAAAACs1iGIbh7BDOlpmZKT8/P2VkZBTt67u37HZ2AgDA3Wj5sLMT3FdWHTnr7AgAADv1qFnR2RFuq7A9sshe0w0AAAAAQHFH6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAkTi3dW7duVZcuXRQSEiKLxaI1a9ZYt127dk2vvvqq6tatKx8fH4WEhKhPnz46c+aMzTFycnI0ZMgQlS9fXj4+PuratatOnz59jz8JAAAAAAAFObV0X758WZGRkUpISCiw7cqVK9qzZ4/GjRunPXv2aNWqVTp69Ki6du1qs19MTIxWr16tDz74QNu3b1dWVpY6d+6svLy8e/UxAAAAAAC4KTdnvnmHDh3UoUOHm27z8/NTYmKizdh7772nRx99VKdOnVKVKlWUkZGhhQsXaunSpWrTpo0kadmyZQoNDdUXX3yhdu3amf4ZAAAAAAC4lWJ1TXdGRoYsFovKli0rSUpKStK1a9fUtm1b6z4hISGKiIjQjh07nJQSAAAAAIDfOHWm+05cvXpVo0ePVq9evVSmTBlJUmpqqjw8POTv72+zb1BQkFJTU295rJycHOXk5FjXMzMzzQkNAAAAALivFYuZ7mvXrunpp59Wfn6+5syZc9v9DcOQxWK55fb4+Hj5+flZl9DQUEfGBQAAAABAUjEo3deuXVPPnj2VnJysxMRE6yy3JAUHBys3N1fp6ek2r0lLS1NQUNAtjzlmzBhlZGRYl5SUFNPyAwAAAADuX0W6dN8o3MeOHdMXX3yhgIAAm+2NGjWSu7u7zQ3Xzp49q4MHD6pp06a3PK6np6fKlCljswAAAAAA4GhOvaY7KytLx48ft64nJydr3759KleunEJCQvTEE09oz549Wrt2rfLy8qzXaZcrV04eHh7y8/NT//79FRsbq4CAAJUrV04jRoxQ3bp1rXczBwAAAADAWZxaunfv3q1WrVpZ14cPHy5J6tu3ryZMmKBPPvlEklS/fn2b123atElRUVGSpHfeeUdubm7q2bOnsrOz1bp1ay1evFiurq735DMAAAAAAHArFsMwDGeHcLbMzEz5+fkpIyOjaJ9qvmW3sxMAAO5Gy4edneC+surIWWdHAADYqUfNis6OcFuF7ZFF+ppuAAAAAACKM0o3AAAAAAAmoXQDAAAAAGASSjcAAAAAACahdAMAAAAAYBJKNwAAAAAAJqF0AwAAAABgEko3AAAAAAAmoXQDAAAAAGASSjcAAAAAACahdAMAAAAAYBJKNwAAAAAAJqF0AwAAAABgErc7fUFGRoZWr16tbdu26eTJk7py5YoqVKigBg0aqF27dmratKkZOQEAAAAAKHYKPdN99uxZ/e1vf1PFihU1ceJEXb58WfXr11fr1q1VuXJlbdq0SdHR0apTp45WrFhhZmYAAAAAAIqFQs90R0ZGqk+fPvr2228VERFx032ys7O1Zs0azZgxQykpKRoxYoTDggIAAAAAUNwUunQfOnRIFSpU+MN9vLy89Mwzz+iZZ57RuXPn7jocAAAAAADFWaFPL79d4b7b/QEAAAAAKGnsunv5kiVLtG7dOuv6qFGjVLZsWTVt2lQ//fSTw8IBAAAAAFCc2VW64+Li5OXlJUn6+uuvlZCQoGnTpql8+fIaNmyYQwMCAAAAAFBc3fEjwyQpJSVFNWrUkCStWbNGTzzxhAYMGKBmzZopKirKkfkAAAAAACi27JrpLl26tC5cuCBJ2rBhg9q0aSNJKlWqlLKzsx2XDgAAAACAYsyume7o6Gi98MILatCggY4ePapOnTpJ+u0O59WqVXNkPgAAAAAAii27Zrpnz56tJk2a6Ny5c1q5cqUCAgIkSUlJSXrmmWccGhAAAAAAgOLKrpnusmXLKiEhocD4G2+8cdeBAAAAAAAoKQpduvfv31/og9arV8+uMAAAAAAAlCSFLt3169eXxWKRYRiyWCx/uG9eXt5dBwMAAAAAoLgr9DXdycnJ+vHHH5WcnKyVK1cqLCxMc+bM0d69e7V3717NmTNHDzzwgFauXGlmXgAAAAAAio1Cz3RXrVrV+vOTTz6pd999Vx07drSO1atXT6GhoRo3bpy6devm0JAAAAAAABRHdt29/MCBAwoLCyswHhYWpsOHD991KAAAAAAASgK7Snft2rX15ptv6urVq9axnJwcvfnmm6pdu7bDwgEAAAAAUJzZ9ciwefPmqUuXLgoNDVVkZKQk6bvvvpPFYtHatWsdGhAAAAAAgOLKrtL96KOPKjk5WcuWLdMPP/wgwzD01FNPqVevXvLx8XF0RgAAAAAAiiW7SrckeXt7a8CAAY7MAgAAAABAiWJ36T569Kg2b96stLQ05efn22wbP378XQcDAAAAAKC4s6t0v//++3r55ZdVvnx5BQcHy2KxWLdZLBZKNwAAAAAAsrN0v/nmm5o8ebJeffVVR+cBAAAAAKDEsOuRYenp6XryyScdnQUAAAAAgBLFrtL95JNPasOGDY7OAgAAAABAiWLX6eU1atTQuHHjtHPnTtWtW1fu7u4224cOHeqQcAAAAAAAFGd2le4FCxaodOnS2rJli7Zs2WKzzWKxULoBAAAAAJCdpTs5OdnROQAAAAAAKHHsuqYbAAAAAADcnt2l+/Tp05ozZ45Gjx6t4cOH2yyFtXXrVnXp0kUhISGyWCxas2aNzXbDMDRhwgSFhITIy8tLUVFROnTokM0+OTk5GjJkiMqXLy8fHx917dpVp0+ftvdjAQAAAADgMHaV7o0bN6pmzZqaM2eO3n77bW3atEmLFi3SP//5T+3bt6/Qx7l8+bIiIyOVkJBw0+3Tpk3TjBkzlJCQoF27dik4OFjR0dG6dOmSdZ+YmBitXr1aH3zwgbZv366srCx17txZeXl59nw0AAAAAAAcxq7SPWbMGMXGxurgwYMqVaqUVq5cqZSUFLVs2fKOnt/doUMHvfnmm+rRo0eBbYZhaObMmRo7dqx69OihiIgILVmyRFeuXNHy5cslSRkZGVq4cKHefvtttWnTRg0aNNCyZct04MABffHFF/Z8NAAAAAAAHMau0v3999+rb9++kiQ3NzdlZ2erdOnSmjhxoqZOneqQYMnJyUpNTVXbtm2tY56enmrZsqV27NghSUpKStK1a9ds9gkJCVFERIR1HwAAAAAAnMWu0u3j46OcnBxJv5XcEydOWLedP3/eIcFSU1MlSUFBQTbjQUFB1m2pqany8PCQv7//Lfe5mZycHGVmZtosAAAAAAA4ml2l+7HHHtNXX30lSerUqZNiY2M1efJk9evXT4899phDA1osFpt1wzAKjP232+0THx8vPz8/6xIaGuqQrAAAAAAA/J5dpXvGjBlq3LixJGnChAmKjo7WihUrVLVqVS1cuNAhwYKDgyWpwIx1WlqadfY7ODhYubm5Sk9Pv+U+NzNmzBhlZGRYl5SUFIdkBgAAAADg9+wq3dWrV1e9evUkSd7e3pozZ47279+vVatWqWrVqg4JFhYWpuDgYCUmJlrHcnNztWXLFjVt2lSS1KhRI7m7u9vsc/bsWR08eNC6z814enqqTJkyNgsAAAAAAI7mZs+LUlJSZLFYVLlyZUnSt99+q+XLl6tOnToaMGBAoY+TlZWl48ePW9eTk5O1b98+lStXTlWqVFFMTIzi4uIUHh6u8PBwxcXFydvbW7169ZIk+fn5qX///oqNjVVAQIDKlSunESNGqG7dumrTpo09Hw0AAAAAAIexq3T36tVLAwYMUO/evZWamqo2bdooIiJCy5YtU2pqqsaPH1+o4+zevVutWrWyrg8fPlyS1LdvXy1evFijRo1Sdna2Bg4cqPT0dDVu3FgbNmyQr6+v9TXvvPOO3Nzc1LNnT2VnZ6t169ZavHixXF1d7floAAAAAAA4jMUwDONOX+Tv76+dO3eqZs2aevfdd7VixQp99dVX2rBhg1566SX9+OOPZmQ1TWZmpvz8/JSRkVG0TzXfstvZCQAAd6Plw85OcF9ZdeSssyMAAOzUo2ZFZ0e4rcL2SLuu6b527Zo8PT0lSV988YW6du0qSapVq5bOnuUXHAAAAAAAkp2l+6GHHtK8efO0bds2JSYmqn379pKkM2fOKCAgwKEBAQAAAAAoruwq3VOnTtX8+fMVFRWlZ555RpGRkZKkTz75RI8++qhDAwIAAAAAUFzZdSO1qKgonT9/XpmZmfL397eODxgwQN7e3g4LBwAAAABAcWZX6ZYkV1dXm8ItSdWqVbvbPAAAAAAAlBh2le6wsDBZLJZbbi9udy8HAAAAAMAMdpXumJgYm/Vr165p7969+vzzzzVy5EhH5AIAAAAAoNizq3S/8sorNx2fPXu2du/mWdIAAAAAAEh23r38Vjp06KCVK1c68pAAAAAAABRbDi3dH330kcqVK+fIQwIAAAAAUGzZdXp5gwYNbG6kZhiGUlNTde7cOc2ZM8dh4QAAAAAAKM7sKt3dunWzWXdxcVGFChUUFRWlWrVqOSIXAAAAAADFnl2l+/XXX3d0DgAAAAAAShy7Srck5eXlac2aNfr+++9lsVhUp04dde3aVa6uro7MBwAAAABAsWVX6T5+/Lg6duyon3/+WTVr1pRhGDp69KhCQ0O1bt06PfDAA47OCQAAAABAsWPX3cuHDh2qBx54QCkpKdqzZ4/27t2rU6dOKSwsTEOHDnV0RgAAAAAAiiW7Zrq3bNminTt32jweLCAgQFOmTFGzZs0cFg4AAAAAgOLMrpluT09PXbp0qcB4VlaWPDw87joUAAAAAAAlgV2lu3PnzhowYIC++eYbGYYhwzC0c+dOvfTSS+rataujMwIAAAAAUCzZVbrfffddPfDAA2rSpIlKlSqlUqVKqVmzZqpRo4ZmzZrl6IwAAAAAABRLdl3TXbZsWX388cc6duyYfvjhBxmGoTp16qhGjRqOzgcAAAAAQLFl93O6JSk8PFzh4eGOygIAAAAAQIliV+nOy8vT4sWLtXHjRqWlpSk/P99m+5dffumQcAAAAAAAFGd2le5XXnlFixcvVqdOnRQRESGLxeLoXAAAAAAAFHt2le4PPvhAH374oTp27OjoPAAAAAAAlBh23b3cw8ODm6YBAAAAAHAbdpXu2NhYzZo1S4ZhODoPAAAAAAAlRqFPL+/Ro4fN+pdffqn//Oc/euihh+Tu7m6zbdWqVY5JBwAAAABAMVbo0u3n52ez3r17d4eHAQAAAACgJCl06V60aJGZOQAAAAAAKHHsuqb78ccf16+//lpgPDMzU48//vjdZgIAAAAAoESwq3Rv3rxZubm5BcavXr2qbdu23XUoAAAAAABKgjt6Tvf+/futPx8+fFipqanW9by8PH3++eeqVKmS49IBAAAAAFCM3VHprl+/viwWiywWy01PI/fy8tJ7773nsHAAAAAAABRnd1S6k5OTZRiGqlevrm+//VYVKlSwbvPw8FBgYKBcXV0dHhIAAAAAgOLojkp31apVJUn5+fmmhAEAAAAAoCSx60ZqAAAAAADg9ijdAAAAAACYhNINAAAAAIBJKN0AAAAAAJjkjm6k9t9yc3OVlpZW4MZqVapUuatQAAAAAACUBHaV7mPHjqlfv37asWOHzbhhGLJYLMrLy3NIOAAAAAAAijO7Svdzzz0nNzc3rV27VhUrVpTFYnF0LgAAAAAAij27runet2+f5s+frw4dOqh+/fqKjIy0WRzl+vXreu211xQWFiYvLy9Vr15dEydOtDmd3TAMTZgwQSEhIfLy8lJUVJQOHTrksAwAAAAAANjLrtJdp04dnT9/3tFZCpg6darmzZunhIQEff/995o2bZqmT5+u9957z7rPtGnTNGPGDCUkJGjXrl0KDg5WdHS0Ll26ZHo+AAAAAAD+iF2le+rUqRo1apQ2b96sCxcuKDMz02ZxlK+//lp//vOf1alTJ1WrVk1PPPGE2rZtq927d0v6bZZ75syZGjt2rHr06KGIiAgtWbJEV65c0fLlyx2WAwAAAAAAe9hVutu0aaOdO3eqdevWCgwMlL+/v/z9/VW2bFn5+/s7LFzz5s21ceNGHT16VJL03Xffafv27erYsaMkKTk5WampqWrbtq31NZ6enmrZsmWBm7wBAAAAAHCv2XUjtU2bNjk6x029+uqrysjIUK1ateTq6qq8vDxNnjxZzzzzjCQpNTVVkhQUFGTzuqCgIP3000+3PG5OTo5ycnKs646cnQcAAAAA4Aa7SnfLli0dneOmVqxYoWXLlmn58uV66KGHtG/fPsXExCgkJER9+/a17vffd0+/8eiyW4mPj9cbb7xhWm4AAAAAAKQ7KN379+9XRESEXFxctH///j/ct169encdTJJGjhyp0aNH6+mnn5Yk1a1bVz/99JPi4+PVt29fBQcHS/ptxrtixYrW16WlpRWY/f69MWPGaPjw4db1zMxMhYaGOiQzAAAAAAA3FLp0169fX6mpqQoMDFT9+vVlsVhkGEaB/SwWi/Ly8hwS7sqVK3Jxsb3s3NXV1frIsLCwMAUHBysxMVENGjSQJOXm5mrLli2aOnXqLY/r6ekpT09Ph2QEAAAAAOBWCl26k5OTVaFCBevP90KXLl00efJkValSRQ899JD27t2rGTNmqF+/fpJ+K/gxMTGKi4tTeHi4wsPDFRcXJ29vb/Xq1eueZAQAAAAA4FYKXbqrVq1605/N9N5772ncuHEaOHCg0tLSFBISohdffFHjx4+37jNq1ChlZ2dr4MCBSk9PV+PGjbVhwwb5+vrek4wAAAAAANyKxbjZOeI38fXXX6tJkyaFOujly5d18uRJPfTQQ3cV7l7JzMyUn5+fMjIyVKZMGWfHubUtu52dAABwN1o+7OwE95VVR846OwIAwE49ala8/U5OVtgeWejndPfp00fR0dH68MMPlZWVddN9Dh8+rL///e+qUaOG9uzZc+epAQAAAAAoQQp9evnhw4c1f/58jR8/Xs8++6wefPBBhYSEqFSpUkpPT9cPP/ygy5cvq0ePHkpMTFRERISZuQEAAAAAKPIKfXr57+3Zs0fbtm3TyZMnlZ2drfLly6tBgwZq1aqVypUrZ0ZOU3F6OQDgnuD08nuK08sBoPgqSaeXF3qm+/caNmyohg0b2h0OAAAAAID7QaGv6QYAAAAAAHeG0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYpNB3L3/33XcLfdChQ4faFQYAAAAAgJKk0KX7nXfeKdR+FouF0g0AAAAAgO6gdCcnJ5uZAwAAAACAEodrugEAAAAAMEmhZ7r/2+nTp/XJJ5/o1KlTys3Ntdk2Y8aMuw4GAAAAAEBxZ1fp3rhxo7p27aqwsDAdOXJEEREROnnypAzDUMOGDR2dEQAAAACAYsmu08vHjBmj2NhYHTx4UKVKldLKlSuVkpKili1b6sknn3R0RgAAAAAAiiW7Svf333+vvn37SpLc3NyUnZ2t0qVLa+LEiZo6dapDAwIAAAAAUFzZVbp9fHyUk5MjSQoJCdGJEyes286fP++YZAAAAAAAFHN2XdP92GOP6auvvlKdOnXUqVMnxcbG6sCBA1q1apUee+wxR2cEAAAAAKBYsqt0z5gxQ1lZWZKkCRMmKCsrSytWrFCNGjX0zjvvODQgAAAAAADFlV2lu3r16tafvb29NWfOHIcFAgAAAACgpLDrmu7q1avrwoULBcZ//fVXm0IOAAAAAMD9zK7SffLkSeXl5RUYz8nJ0c8//3zXoQAAAAAAKAnu6PTyTz75xPrz+vXr5efnZ13Py8vTxo0bVa1aNYeFAwAAAACgOLuj0t2tWzdJksVisT6n+wZ3d3dVq1ZNb7/9tsPCAQAAAABQnN1R6c7Pz5ckhYWFadeuXSpfvrwpoQAAAAAAKAnsunt5cnKyo3MAAAAAAFDi2HUjNUnasmWLunTpoho1aig8PFxdu3bVtm3bHJkNAAAAAIBiza7SvWzZMrVp00be3t4aOnSoBg8eLC8vL7Vu3VrLly93dEYAAAAAAIolu04vnzx5sqZNm6Zhw4ZZx1555RXNmDFDkyZNUq9evRwWEAAAAACA4squme4ff/xRXbp0KTDetWtXrvcGAAAAAOD/2FW6Q0NDtXHjxgLjGzduVGho6F2HAgAAAACgJLij08v79eunWbNmKTY2VkOHDtW+ffvUtGlTWSwWbd++XYsXL9asWbPMygoAAAAAQLFyR6V7yZIlmjJlil5++WUFBwfr7bff1ocffihJql27tlasWKE///nPpgQFAAAAAKC4uaPSbRiG9efu3bure/fuDg8EAAAAAEBJccfXdFssFjNyAAAAAABQ4tzxI8MefPDB2xbvixcv2h0IAAAAAICS4o5L9xtvvCE/Pz8zsgAAAAAAUKLccel++umnFRgYaEYWAAAAAABKlDu6ppvruQEAAAAAKLw7Kt2/v3s5AAAAAAD4Y3d0enl+fr5ZOQAAAAAAKHHu+JFhAAAAAACgcIp86f7555/117/+VQEBAfL29lb9+vWVlJRk3W4YhiZMmKCQkBB5eXkpKipKhw4dcmJiAAAAAAB+U6RLd3p6upo1ayZ3d3f95z//0eHDh/X222+rbNmy1n2mTZumGTNmKCEhQbt27VJwcLCio6N16dIl5wUHAAAAAEB2PDLsXpo6dapCQ0O1aNEi61i1atWsPxuGoZkzZ2rs2LHq0aOHJGnJkiUKCgrS8uXL9eKLL97ryAAAAAAAWBXpme5PPvlEDz/8sJ588kkFBgaqQYMGev/9963bk5OTlZqaqrZt21rHPD091bJlS+3YscMZkQEAAAAAsCrSpfvHH3/U3LlzFR4ervXr1+ull17S0KFD9a9//UuSlJqaKkkKCgqyeV1QUJB1283k5OQoMzPTZgEAAAAAwNGK9Onl+fn5evjhhxUXFydJatCggQ4dOqS5c+eqT58+1v0sFovN6wzDKDD2e/Hx8XrjjTfMCQ0AAAAAwP8p0jPdFStWVJ06dWzGateurVOnTkmSgoODJanArHZaWlqB2e/fGzNmjDIyMqxLSkqKg5MDAAAAAFDES3ezZs105MgRm7GjR4+qatWqkqSwsDAFBwcrMTHRuj03N1dbtmxR06ZNb3lcT09PlSlTxmYBAAAAAMDRivTp5cOGDVPTpk0VFxennj176ttvv9WCBQu0YMECSb+dVh4TE6O4uDiFh4crPDxccXFx8vb2Vq9evZycHgAAAABwvyvSpfuRRx7R6tWrNWbMGE2cOFFhYWGaOXOmnn32Wes+o0aNUnZ2tgYOHKj09HQ1btxYGzZskK+vrxOTAwAAAAAgWQzDMJwdwtkyMzPl5+enjIyMon2q+Zbdzk4AALgbLR92doL7yqojZ50dAQBgpx41Kzo7wm0VtkcW6Wu6AQAAAAAozijdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASYpV6Y6Pj5fFYlFMTIx1zDAMTZgwQSEhIfLy8lJUVJQOHTrkvJAAAAAAAPyfYlO6d+3apQULFqhevXo249OmTdOMGTOUkJCgXbt2KTg4WNHR0bp06ZKTkgIAAAAA8JtiUbqzsrL07LPP6v3335e/v7913DAMzZw5U2PHjlWPHj0UERGhJUuW6MqVK1q+fLkTEwMAAAAAUExK96BBg9SpUye1adPGZjw5OVmpqalq27atdczT01MtW7bUjh077nVMAAAAAABsuDk7wO188MEH2rNnj3bt2lVgW2pqqiQpKCjIZjwoKEg//fTTLY+Zk5OjnJwc63pmZqaD0gIAAAAA8P8V6ZnulJQUvfLKK1q2bJlKlSp1y/0sFovNumEYBcZ+Lz4+Xn5+ftYlNDTUYZkBAAAAALihSJfupKQkpaWlqVGjRnJzc5Obm5u2bNmid999V25ubtYZ7hsz3jekpaUVmP3+vTFjxigjI8O6pKSkmPo5AAAAAAD3pyJ9ennr1q114MABm7Hnn39etWrV0quvvqrq1asrODhYiYmJatCggSQpNzdXW7Zs0dSpU295XE9PT3l6epqaHQAAAACAIl26fX19FRERYTPm4+OjgIAA63hMTIzi4uIUHh6u8PBwxcXFydvbW7169XJGZAAAAAAArIp06S6MUaNGKTs7WwMHDlR6eroaN26sDRs2yNfX19nRAAAAAAD3OYthGIazQzhbZmam/Pz8lJGRoTJlyjg7zq1t2e3sBACAu9HyYWcnuK+sOnLW2REAAHbqUbOisyPcVmF7ZJG+kRoAAAAAAMUZpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADBJkS7d8fHxeuSRR+Tr66vAwEB169ZNR44csdnHMAxNmDBBISEh8vLyUlRUlA4dOuSkxAAAAAAA/H9FunRv2bJFgwYN0s6dO5WYmKjr16+rbdu2unz5snWfadOmacaMGUpISNCuXbsUHBys6OhoXbp0yYnJAQAAAACQ3Jwd4I98/vnnNuuLFi1SYGCgkpKS1KJFCxmGoZkzZ2rs2LHq0aOHJGnJkiUKCgrS8uXL9eKLLzojNgAAAAAAkor4TPd/y8jIkCSVK1dOkpScnKzU1FS1bdvWuo+np6datmypHTt23PI4OTk5yszMtFkAAAAAAHC0YlO6DcPQ8OHD1bx5c0VEREiSUlNTJUlBQUE2+wYFBVm33Ux8fLz8/PysS2hoqHnBAQAAAAD3rWJTugcPHqz9+/fr3//+d4FtFovFZt0wjAJjvzdmzBhlZGRYl5SUFIfnBQAAAACgSF/TfcOQIUP0ySefaOvWrapcubJ1PDg4WNJvM94VK1a0jqelpRWY/f49T09PeXp6mhcYAAAAAAAV8ZluwzA0ePBgrVq1Sl9++aXCwsJstoeFhSk4OFiJiYnWsdzcXG3ZskVNmza913EBAAAAALBRpGe6Bw0apOXLl+vjjz+Wr6+v9TptPz8/eXl5yWKxKCYmRnFxcQoPD1d4eLji4uLk7e2tXr16OTk9AAAAAOB+V6RL99y5cyVJUVFRNuOLFi3Sc889J0kaNWqUsrOzNXDgQKWnp6tx48basGGDfH1973FaAAAAAABsFenSbRjGbfexWCyaMGGCJkyYYH4gAAAAAADuQJG+phsAAAAAgOKM0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAAAAAACYhNINAAAAAIBJKN0AAAAAAJikxJTuOXPmKCwsTKVKlVKjRo20bds2Z0cCAAAAANznSkTpXrFihWJiYjR27Fjt3btXf/rTn9ShQwedOnXK2dEAAAAAAPexElG6Z8yYof79++uFF15Q7dq1NXPmTIWGhmru3LnOjgYAAAAAuI+5OTvA3crNzVVSUpJGjx5tM962bVvt2LHjpq/JyclRTk6OdT0jI0OSlJmZaV5QR7ic5ewEAIC7UdR/z5QwV7IuOTsCAMBOmZk+zo5wWzf6o2EYf7hfsS/d58+fV15enoKCgmzGg4KClJqaetPXxMfH64033igwHhoaakpGAAAAAEDJdOnSJfn5+d1ye7Ev3TdYLBabdcMwCozdMGbMGA0fPty6np+fr4sXLyogIOCWrwFgrszMTIWGhiolJUVlypRxdhwAAIo0fm8CzmcYhi5duqSQkJA/3K/Yl+7y5cvL1dW1wKx2WlpagdnvGzw9PeXp6WkzVrZsWbMiArgDZcqU4T8PAAAUEr83Aef6oxnuG4r9jdQ8PDzUqFEjJSYm2ownJiaqadOmTkoFAAAAAEAJmOmWpOHDh6t37956+OGH1aRJEy1YsECnTp3SSy+95OxoAAAAAID7WIko3U899ZQuXLigiRMn6uzZs4qIiNBnn32mqlWrOjsagELy9PTU66+/XuDSDwAAUBC/N4Hiw2Lc7v7mAAAAAADALsX+mm4AAAAAAIoqSjcAAAAAACahdAMAAAAAYBJKNwAAAAAAJqF0AwAAAABgEko3AAAAAAAmoXQDAAAAAGASSjeAYskwDGdHAACgyOP3JeB8bs4OAAB3yjAMWSwWbd68Wdu2bdOhQ4fUt29f1alTR1WrVnV2PAAA7rkbvxuTkpJ09OhRnTt3Tn/5y19UqVIlZ0cD7nvMdAModiwWi1atWqVu3brp+PHj8vLy0gsvvKBx48bpl19+cXY8AADuOYvFopUrV6pr166aPXu2PvroIz344INavny5cnNznR0PuK8x0w2g2LjxV/wff/xRY8eO1VtvvaUXXnhBeXl58vb2VtWqVRUUFOTsmAAA3HN79+7Vyy+/rClTpqhfv366cOGCKlSooFOnTsnDw8PZ8YD7GjPdAIq0NWvWaOfOnZJ++yu+JOXm5srHx0f9+/fXkSNHVK1aNfXp00eTJk2SJB04cEBXr151WmYAAMz0zTffFBg7c+aMmjZtqn79+unYsWNq0KCB/va3v2n06NGSpOzsbElc4w04A6UbQJFkGIZ+/vlnPf/883rrrbeUlJRk3Xb69GmdO3dOx44dU8eOHdWhQwfNnz9f0m//EZk5c6ZOnz7trOgAAJgmKSlJTZo00bRp02zGf/jhB505c0Y///yzoqOj1aFDB82dO1eStGrVKsXExCgnJ8f6B2wA9w6lG0CRZLFYVKlSJa1du1YHDhzQtGnTtHv3bklSmzZtVK1aNdWqVUstWrTQggUL5OLy2z9nq1ev1pEjR1SmTBlnxgcAwBSNGjXSzJkzNW7cOL311lvWmev27dvL3d1dtWrV0uOPP279Y7Qk7dy5U2fPnuUsMMBJuKYbQJGVn5+vZs2aadGiRerdu7emT5+uESNG6JFHHtGIESN05coVHTt2TD/88INOnz6t9evXa/78+dq+fbsCAwOdHR8AAFMMHTpUrq6uGjJkiAzD0MiRIxUWFqaGDRvq7Nmzqlq1qq5du6ZTp05p4cKFWrhwobZu3So/Pz9nRwfuSxaDCzsAFGH5+flycXHRjh071Lt3bzVq1Ejjxo1TRESE/vOf/2jKlCnau3evQkNDVa5cOc2ePVuRkZHOjg0AgOlmz56tIUOGKC4uTqNHj9avv/6qsWPHavPmzTp58qRq166trKws/fvf/1aDBg2cHRe4b1G6ARQ5N+5S/t+2b9+uvn37qmHDhho/frzq1q0r6bfr2ypXriwPDw/5+/vf67gAADhNQkKChg4dqsmTJ2vMmDG6evWqfvnlF3311Vd68MEHValSJVWsWNHZMYH7GqUbQJFyo3B//fXX2rdvn3755Rc9/fTTqlKliry9va3Fu1GjRho5cqQeeeQRZ0cGAMBUN343Hjx4UGlpacrMzFS3bt2s228U7xsz3gCKFko3gCLjxn8qVq1apX79+ql58+Y6duyY/P399cwzz+j5559XmTJltH37dr3wwguqXr264uLiVL9+fWdHBwDAFDd+N65evVpDhw6Vv7+/UlJS9Oijj+qtt97SQw89JBcXFyUkJGjEiBEaM2aMxo8fz13KgSKEu5cDKDIsFou2b9+uwYMHa8aMGVq7dq2+/PJLJSUlaeHChZo7d64uXbqk5s2ba+7cuUpNTVWFChWcHRsAAIfJz8+3WbdYLPriiy/Uv39/TZgwQfv379fGjRuVmJiomJgY7du3T4ZhaPDgwZo0aZLeffddpaenOyk9gJthphtAkZGfn6/3339fhw8f1qxZs/Tjjz8qOjpaLVu21PXr17V+/XqNGjVK/fv3V9myZZWdnS0vLy9nxwYAwCFu3Dz05MmT2r9/v7p27arc3Fy9+uqr8vPz04QJE5ScnKw2bdqoRYsW2rp1qwIDA5WQkKAGDRrIxcVF6enp3N8EKGIo3QCKlOTkZOXk5Khq1arq1KmTwsLCtHDhQmVlZemBBx5Q6dKlNWjQIA0bNkySOH0OAFCinDlzRpGRkapQoYJee+019erVS4mJiapUqZJCQkLUtm1bRUZG6v3339emTZvUunVrNWzYUAsXLuTpHUARxXO6ATjNjevUfn+38qpVq8rFxUX79+9XWlqa4uPjJUmnT5/WI488osqVK+svf/kLZRsAUCIdOXJEFy5cUFhYmFasWCEXFxc9/fTTkqSPP/5YkvTqq69Kkq5evaouXbooJSVFvr6+TssM4I9xTTcAp7hRtD///HM999xzGjx4sDZs2CAXl9/+Wbp8+bKuXr2qY8eOKTMzUytWrJCXl5feeustVa1a1cnpAQAwR6tWrfT8888rNzdX7u7uWrBggZYuXSpJSktL05kzZ6yXVm3fvl3169fXrl27VL16dWfGBvAHOL0cgNNs3LhR3bp1U3R0tC5evKgdO3Zo7ty56t+/v65cuaKnnnpKBw8elKurq3799Vdt2LBBDRs2dHZsAAAc4sY13Dfk5OTI09NTn332mf73f/9XzzzzjObPn6/z589r2LBhioqKUkREhEqVKqXg4GAdPHhQmzdv5ikeQBFH6QbgNIsWLdKlS5c0dOhQnTt3TvPnz9f48eM1e/Zsvfzyy8rKytKnn36qa9euqVmzZnrggQecHRkAAIe4UbhTUlKUlJRk89ztc+fOqUWLFho8eLB69uypl156Sb/88otGjx6tRx99VNOnT5e7u7t69+6t2rVrO+9DACgUSjeAe+bGKeUHDx7UpUuXNGvWLLVq1UovvviipN9OKZ85c6bGjRtnLd4AAJRUKSkpatCggS5evKgOHTqob9++ql+/vh588EF9+umnmj59ulauXKnz58/rtdde08WLFzVo0CA98cQTzo4O4A5wTTeAe8ZisWj16tV6+OGH9be//U0rV67UgQMHlJubK0ny8fHRsGHDFBcXp0GDBmnx4sXODQwAgIny8/MVFhamxx57TL/88osSExPVtm1bzZ8/X9nZ2fLz89Pu3btVu3ZtTZo0SW5ublqyZIkyMzOdHR3AHWCmG4Dpbsxwnz17Vk888YT69eunyMhIbdmyRSNHjtS0adM0fPhwm5uozZ8/Xx06dOC0OQBAiXbs2DGNHj1a+fn56tOnj1xcXDRz5kyVLVtWH3/8sR555BFt27ZNHh4eOnLkiHx8fFS5cmVnxwZwByjdAO6J9evXa/369UpLS9PcuXOtjzaZPXu2hgwZoqlTpyo2NtbmhjIAANwPjhw5omHDhikvL0/vvfeeKlWqpAMHDmjy5Mnq2bOnevfubfN4TQDFC6UbwD2xZMkSPf/88/L399dXX32lWrVqWbfNnj1bsbGx+vvf/65x48bxnwoAwH3n2LFjGjx4sCRp/PjxatasmZMTAXAUppQA3BN9+/bVihUrlJ6ern/84x+6cOGCddugQYM0efJkzZo1S+np6U5MCQCAc4SHhyshIUEuLi6aNGmStm/f7uxIAByEmW4ADnXjnxSLxaITJ07o/PnzysvLU6NGjeTp6al//vOfeuGFFzR69GjFxsYqICDA+tr09HT5+/s7KzoAAE537NgxDR8+XOfPn9c777yjxx57zNmRANwlN2cHAFDyWCwWrVq1SmPHjtX169dVvnx5XblyRYmJierXr5/c3Nz03HPPydXVVa+88orKly8vSRRuAMB9Lzw8XNOnT9e4ceMUEhLi7DgAHIDTywHclfz8fEnSlStXJP1WuLdu3aq+fftq2LBhOnTokMaOHasDBw7of/7nf2QYhvr06aPFixdr8uTJmjt3rvUYAABAqlWrlv7nf/5HVapUcXYUAA7A6eUA7Jafny8XFxclJSXpqaee0hdffKFq1arprbfe0k8//aT33ntPKSkpat68ubp06aKEhARJ0rVr1+Tu7q5///vfioyMVJ06dZz8SQAAAABzMNMNwC43Cvd3332nVq1aqUuXLqpWrZok6fDhw7p69arOnDmjpk2bqn379nrvvfckSR999JHeffdd5eXl6ZlnnqFwAwAAoESjdAO4YzcK9/79+9W0aVMNGTJE77zzjnV73bp1deHCBT3yyCNq37695s+fL+m3Ge5Nmzbp9OnTys3NdVZ8AAAA4J7hRmoA7piLi4tSUlLUunVrde7cWZMnT7Zue//99/Xtt99q//79unr1qvr16ydJunz5suLj47V69Wpt2rRJXl5ezooPAAAA3DOUbgB2ycvLU1hYmK5evaqvvvpKzZo1U3x8vN58803t2rVLZcqUUYsWLTR48GBdunRJNWrU0L59+7Ru3TrVrFnT2fEBAACAe4IbqQGw27FjxzR06FB5eHgoKChIH3/8sZYuXaq2bdtKklJTU7Vp0yYdOHBAERERatKkicLCwpycGgAAALh3KN0A7srRo0c1ePBgbd++XZMmTVJsbKwk6fr163Jz42QaAAAA3N8o3QDu2okTJzRw4EC5urrq73//u5o3by5JMgxDFovFyekAAAAA5+Hu5QDu2gMPPKCEhAQZhqE333xTX331lSRRuAEAAHDfo3QDcIjw8HC9++67cnd314gRI7Rz505nRwIAAACcjtINwGHCw8M1ffp0Va5cWSEhIc6OAwAAADgd13QDcLjc3Fx5eHg4OwYAAADgdJRuAAAAAABMwunlAAAAAACYhNINAAAAAIBJKN0AAAAAAJiE0g0AAAAAgEko3QAAAAAAmITSDQAAAACASSjdAADgrkRFRSkmJsbZMQAAKJIo3QAAlACpqal65ZVXVKNGDZUqVUpBQUFq3ry55s2bpytXrjg7HgAA9y03ZwcAAAB358cff1SzZs1UtmxZxcXFqW7durp+/bqOHj2qf/7znwoJCVHXrl2dHfOW8vLyZLFY5OLCXAAAoOThtxsAAMXcwIED5ebmpt27d6tnz56qXbu26tatq7/85S9at26dunTpIknKyMjQgAEDFBgYqDJlyujxxx/Xd999Zz3OhAkTVL9+fS1dulTVqlWTn5+fnn76aV26dMm6z+XLl9WnTx+VLl1aFStW1Ntvv10gT25urkaNGqVKlSrJx8dHjRs31ubNm63bFy9erLJly2rt2rWqU6eOPD099dNPP5n3BQEA4ESUbgAAirELFy5ow4YNGjRokHx8fG66j8VikWEY6tSpk1JTU/XZZ58pKSlJDRs2VOvWrXXx4kXrvidOnNCaNWu0du1arV27Vlu2bNGUKVOs20eOHKlNmzZp9erV2rBhgzZv3qykpCSb93v++ef11Vdf6YMPPtD+/fv15JNPqn379jp27Jh1nytXrig+Pl7/+Mc/dOjQIQUGBjr4mwEAoGjg9HIAAIqx48ePyzAM1axZ02a8fPnyunr1qiRp0KBBateunQ4cOKC0tDR5enpKkt566y2tWbNGH330kQYMGCBJys/P1+LFi+Xr6ytJ6t27tzZu3KjJkycrKytLCxcu1L/+9S9FR0dLkpYsWaLKlStb3/fEiRP697//rdOnTyskJESSNGLECH3++edatGiR4uLiJEnXrl3TnDlzFBkZaeK3AwCA81G6AQAoASwWi836t99+q/z8fD377LPKyclRUlKSsrKyFBAQYLNfdna2Tpw4YV2vVq2atXBLUsWKFZWWlibpt0Kdm5urJk2aWLeXK1fOpvDv2bNHhmHowQcftHmfnJwcm/f28PBQvXr17uITAwBQPFC6AQAoxmrUqCGLxaIffvjBZrx69eqSJC8vL0m/zWBXrFjR5trqG8qWLWv92d3d3WabxWJRfn6+JMkwjNvmyc/Pl6urq5KSkuTq6mqzrXTp0tafvby8CvyhAACAkojSDQBAMRYQEKDo6GglJCRoyJAht7yuu2HDhkpNTZWbm5uqVatm13vVqFFD7u7u2rlzp6pUqSJJSk9P19GjR9WyZUtJUoMGDZSXl6e0tDT96U9/sut9AAAoSbiRGgAAxdycOXN0/fp1Pfzww1qxYoW+//57HTlyRMuWLdMPP/wgV1dXtWnTRk2aNFG3bt20fv16nTx5Ujt27NBrr72m3bt3F+p9Spcurf79+2vkyJHauHGjDh48qOeee87mUV8PPvignn32WfXp00erVq1ScnKydu3apalTp+qzzz4z6ysAAKDIYqYbAIBi7oEHHtDevXsVFxenMWPG6PTp0/L09FSdOnU0YsQIDRw4UBaLRZ999pnGjh2rfv366dy5cwoODlaLFi0UFBRU6PeaPn26srKy1LVrV/n6+io2NlYZGRk2+yxatEhvvvmmYmNj9fPPPysgIEBNmjRRx44dHf3RAQAo8ixGYS7QAgAAAAAAd4zTywEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJNQugEAAAAAMAmlGwAAAAAAk1C6AQAAAAAwCaUbAAAAAACTULoBAAAAADAJpRsAAAAAAJP8P2C+B7heHqvcAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "\n",
    "# Assuming that the uploaded file is an image showing a table with gender and corresponding totals.\n",
    "# Since we can't process the image directly to extract data, let's create a DataFrame with example data based on the image provided by the user.\n",
    "data = {\n",
    "    'gender': ['Female', 'Male'],\n",
    "    'TotalPerGender': [167882.92, 155083.82]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Divide the 'TotalPerGender' values by 1000 to show in thousands\n",
    "df['TotalPerGender'] /= 1000\n",
    "\n",
    "# Create a bar chart\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.bar(df['gender'], df['TotalPerGender'], color=['pink', 'lightblue'])\n",
    "plt.title('Total per Gender')\n",
    "plt.xlabel('Gender')\n",
    "plt.ylabel('Total (in thousands)')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "\n",
    "# Save the plot as a .png file\n",
    "output_file = '/mnt/data/bar_chart.png'\n",
    "#plt.savefig(output_file)\n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0d7a593b",
   "metadata": {},
   "outputs": [],
   "source": [
    "path_to_csv3 = \"/Users/barbaracastelo/Desktop/PW/ficheiros/Week4/GroupProject/pl_for_female.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "83238415",
   "metadata": {},
   "outputs": [],
   "source": [
    "female_spending = pd.read_csv(path_to_csv3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "177b0fcb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>product_line</th>\n",
       "      <th>TotalPerProduct</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>18560.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Electronic accessories</td>\n",
       "      <td>27102.02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Home and lifestyle</td>\n",
       "      <td>30036.88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Food and beverages</td>\n",
       "      <td>33170.92</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Fashion accessories</td>\n",
       "      <td>30437.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Sports and travel</td>\n",
       "      <td>28574.72</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             product_line  TotalPerProduct\n",
       "0       Health and beauty         18560.99\n",
       "1  Electronic accessories         27102.02\n",
       "2      Home and lifestyle         30036.88\n",
       "3      Food and beverages         33170.92\n",
       "4     Fashion accessories         30437.40\n",
       "5       Sports and travel         28574.72"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(female_spending)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "2d73eb5e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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vHmzXnvttTjbWbt2rc6dO6eWLVva5gkCAJIsrtOdlHCN3JcL11nG82D/wfPiOt0AANgU1+kGAAAAAMDOCN0AAAAAANgI53QDAIDEwSkKLxdOUQCARMFINwAAAAAANkLoBgAAAADARgjdAAAAAADYCKEbAAAAeIqgoCCVLl1aqVOnlpeXl95++20dO3YsTh+LxfLI2zfffPPY9R45ckTvvvuucuTIIYvFolGjRj2y34QJE5QzZ065urqqZMmS2rJlS2I+PQA2ROgGAAAAnmLTpk3q2LGjduzYoTVr1igqKko1atRQWFiYtc+lS5fi3H744QdZLBa9++67j11veHi4cuXKpSFDhsjb2/uRfebOnatu3bqpT58+2rdvn15//XUFBATo3Llzif48ASQ+Zi8HAAAAnmLlypVx7gcHB8vLy0t79+5VpUqVJOmh0Pzzzz+rSpUqypUr12PXW7p0aZUuXVqS9Pnnnz+yz4gRI9SqVSu1bt1akjRq1CitWrVKEydOVFBQ0DM/JwAvBiPdAAAAQAKFhIRIktKlS/fI5f/884+WLVumVq1aPdd27t27p71796pGjRpx2mvUqKFt27Y917oBvBiEbgAAACABjDHq0aOHKlasqMKFCz+yz/Tp05U6dWq98847z7Wta9euKTo6WpkyZYrTnilTJl2+fPm51g3gxeDwcgAAACABOnXqpIMHD2rr1q2P7fPDDz+ocePGcnV1TZRtWiyWOPeNMQ+1AUiaCN0AAABAPHXu3FlLly7V5s2blTVr1kf22bJli44dO6a5c+c+9/YyZMggR0fHh0a1r1y58tDoN4CkicPLAQAAgKcwxqhTp05atGiR1q9fr5w5cz6279SpU1WyZEkVLVr0ubfr7OyskiVLas2aNXHa16xZo/Llyz/3+gHYHiPdAAAAwFN07NhRs2bN0s8//6zUqVNbR549PT3l5uZm7RcaGqr58+dr+PDhj1xP06ZNlSVLFuus4/fu3dPRo0etP1+4cEH79+9XqlSplDt3bklSjx491KRJE5UqVUrlypXTlClTdO7cObVr186WTxlAIiF0AwAAAE8xceJESVLlypXjtAcHB6t58+bW+3PmzJExRh988MEj13Pu3Dk5OPzfwaYXL15U8eLFrfe//fZbffvtt/L399fGjRslSe+9956uX7+ur776SpcuXVLhwoW1fPly+fr6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unRp7dmzR3v37pXEHACEbuAx7t27p9DQUEVGRurXX39Vr1691LFjRy1YsEAjR47U+PHj7V0ikqioqCidPXtWqVKlUmhoqPr27atGjRrpiy++0HvvvadFixZJ4g3oVTZo0CAtXLhQ0v99YImKipKzs7PKli2refPmKSAgQGPGjFGTJk0UHh6uVatWKSQkxJ5lw84ePA1hwoQJatOmjWrUqKHg4GC5uLioX79+ev3117V8+XImV0OiefC96tatW1q+fLkWLlyod999VxMmTJDFYpGDg4MmTZqkc+fO2bFSvCjGmDhfsCxfvlwVK1bURx99pFWrVikqKkoVK1ZU8+bNNXDgQF25cuWVn9uG0A3o0bOUZ8+eXZUqVdKXX36pBg0ayMvLS4MGDdKxY8fk5eWl69ev26FSJAdp0qRRo0aNFBgYKF9fX508eVJNmjTRjRs3VLZsWa1cuVKSXvk3oFfV6dOnNWfOHAUHB2vZsmXW9ps3b+r27duaPXu22rRpoyFDhqhdu3aSpO3bt+unn37SlStX7FU2koDYwP35559r8ODBSp8+vWrVqqVWrVqpd+/eSp06tXr37q2KFStqxYoV+vTTT+1cMZKz2LAdFRVlnYU6MDBQDRo0UGBgoLJmzarAwEDNnz9fw4YN071793T37l17lowX5OTJk9bXo5kzZ+r69etatGiRzp07p379+um1117TmjVrlDdvXmXIkEGnT5+WJEVHR9uzbLvi5Au88h4cOZg1a5YuXbqkixcvqlOnTvruu+908OBBWSwWFSlSxPqY6Ohoubq62qtkJCGx5zDt3btXx44d05UrV/Tuu+9qwIABql69uq5du6Y333zTGrDTp08vJycnzn97heXKlUvTpk1Tr169NH78eBlj9OabbyogIEC+vr5q3LixxowZo44dO0qSIiIiNHLkSLm4uOh///ufnauHvW3dulXz58/X4sWLVbp0ae3bt099+vTRa6+9Junf15jAwEB99tlnCgkJsb5GAQkRu9+sWrVK3333nS5fvqzs2bMrMDBQs2bN0pUrV+Tl5WXtP3XqVLm5uSljxox2rBovwsGDB1WyZEn98MMPOnLkiCZPnqy9e/cqV65cKlOmjP744w+NGTNGffr0UYoUKbR9+3alS5dOZcuWlaOjo73Ltx8DwBhjzKeffmp8fHxM8+bNTbly5UyOHDnM2LFjTVRUlDHGmJCQEHP48GFTu3ZtU6RIEXP//n07V4ykYsGCBcbHx8dUrFjRVKpUybi5uZkZM2bE6XP27FnzxRdfGE9PT3P48GE7VQp7e/B148CBA6Zy5cqmdu3a5ueffzbGGLNjxw5TsmRJkytXLjNjxgwzevRoU6NGDVOoUCFz7949Y4wx0dHRdqkd9vHf3/fKlStN5cqVjTHGzJkzx6RKlcpMnDjRGPPv+9TOnTuNMcbcvHnTxMTEGGOM9V8gIZYuXWpSpUplevXqZX755ReTJ08eU6hQIXPkyBFrn59//tl07drVpE2b1vz+++92rBYvyqVLl8zAgQONm5ub8fT0NBcuXDDGGBMZGRmn37Zt28yMGTNMoUKFTI4cOczmzZvtUW6SweHlgKSFCxdqzpw5WrFihYKDg9W/f3/99ddfypo1q/VbufXr16tJkya6f/++9u7dKycnp1f6MBn8a9++ferQoYMGDhyoLVu2aNGiRYqIiNDff/9t7fPbb7+pZ8+emjt3rjZu3KhChQrZsWLYU+zRDevWrZOfn5+GDRum8PBwTZo0SatWrVKZMmU0d+5clSxZUkFBQVq4cKGyZcumffv2KUWKFIqKirIemYNXQ+zvO/ayg6GhoTp//rxmzpyptm3batiwYdbTEDZu3KihQ4fq/PnzSpMmjSwWS5zrvwOP8+DnGWOMbt26pW+++UZ9+/bV0KFDVbVqVUVERKhKlSoqWLCgJCkkJEQHDhzQwYMHtXnzZhUvXtxe5eMFiD0V09vbW5kyZVJERITu37+v1atXS/p3ArWYmBjrvlSuXDk1adJEy5Ytk4eHhzZv3my32pMEe6d+ICkYN26cadiwoTHGmFmzZhkPDw8zYcIEY4wxd+7cMWfOnDHGGLNmzRrryDcj3a+edevWPTRitGzZMlOvXj1jjDHHjx832bJlM23atLEuDw8PN+Hh4ebnn3+27kd4dcXExJg9e/YYi8Vi9u/fb4wxZteuXaZy5cqmVq1aZvny5da+ly9fjvM6w2vOq+v77783RYoUMdHR0ebWrVumevXqxmKxmIEDB1r73L1719SrV8988MEHjGwjQXr16mWWLFkSpy00NNSUKFHCXLhwwfz999/Gx8cnznvbqlWrTFhYmImIiDA3btx40SXDjsLDw80///xj9uzZY77++muTOnVq69E2j3vtGTx4sCldurS5ffv2iyw1SeHrcrxyHjVp2smTJ+Xk5KQ9e/aobdu2GjJkiNq3by9Jmj17tqZNm6Z79+6pWrVqcnR0VHR0NOfjvmJ+++031a9fX1evXo3TfuzYMV28eFF///23qlevroCAAE2cOFGStGjRInXr1k0ODg6qV6+ecuTIYYfKkZRYLBaVLFlStWvX1sCBAxUeHq7SpUvr22+/VUREhMaNG6dffvlFkpQpUybr64wxhtecV5iPj49SpEihbdu2ydPTU++//751oqIVK1boxx9/1Ntvv63Tp09rxowZ1hFuID5u3rypnDlzSvq/ydMcHBwUFhamH374Qf7+/qpXr57GjRsnSbp48aJGjBihdevWycXFRWnTprVb7XixvvvuOxUpUsT6XtaiRQt16dJFvXr10nfffWc9qiYoKEh79uyxPu7AgQPy8PB4pd/HCN145cQeqrdjxw5duHBBktSkSROtWrVKr732miZMmGAN3BEREVq8eLGuXr2qFClSWNfxSk8E8YqqUKGCTp06JS8vL50+fdr6gbZmzZpydnZWgQIFVLVqVU2ePNn6mB07dujixYvM5voK+2/wiZ0B+J133tH58+ets5GXLFlS3377rSIjIzVo0CBt27YtzuM4PPjVYR5xKcFy5crJGKMffvhBktSyZUt1795dGTJkUKNGjTR58mSlTZtWv//+u/XUJ05DwNPE7mtTpkyRn5+fVq1apQULFig8PFwpU6ZU48aN9c033yhbtmyaNGmS9XPQhAkTdPHiRRUrVsyO1cMe/P39lSJFCtWuXVvXrl1TlixZ1KFDB3Xt2lWdO3dW586dVb16dQUHB1tPN7h7964OHjyowYMHv9qTENt1nB14gR6cjGbdunUmbdq0JigoyFy5csXcv3/ffPnllyZLliymf//+5uLFi+a3334ztWrVMkWLFrUe1skhe6+mB3/vly5dMhaLxQwYMMAYY0xYWJjp3LmzyZkzp+nXr5+JjIw0J0+eNIGBgSZdunRMmgZjjDGbN282YWFh1vvh4eEmR44cpnPnznH6bd++3XTq1InJ0mCdOC/WmjVrTIYMGczKlSvjtJ87d85ERkZaX6c4DQEJ8eBrTadOnYzFYjELFy40xhhz7Ngx07BhQ5MvXz7Tt29fM3HiRNOmTRvj4eFh9u3bZ6eK8aL8930o9jXm5MmTpnDhwqZ48eLm6tWrxhhjrly5YiZMmGAqVKhgPvzwQ+vrV+y/vC4ZQ+jGK+HB0DRmzBgzdOhQ4+7ubtKmTWsGDx5sbt++bf755x8zbNgwkz59epMhQwbj5+dnatasaX3BiD2XG6+e2P1n48aN5uDBg2bixInGxcXFDB482BhjzK1bt0yHDh1MoUKFjLu7uylRooTJly8fM7nCGPPvef+FChUyuXLlMnPmzDEHDhwwxhgzffp0U6FCBXP48GETExPz0AccgverKygoyNSrV898//331rZr166ZWrVqmb59+xpj/u9D7IP7CV8M41nMmzfPtGrVyhhjTIsWLUyqVKnM/PnzjTHG/Pnnn2bQoEHmf//7nylbtqxp0KCBOXTokD3LxQs2Z84c68//Dd4lS5Y0V65csS5/3BeAvDYRuvGKGTBggPH09DSLFy82S5cuNW3btjVp0qQxQUFB1skdrl+/brZs2WJOnDhh/TDDN3RYv3698fT0tH4QGT9+vLFYLGbQoEHGmH8nMTp79qyZNWuW2bNnj7l48aI9y4Ud7dixw/rz2LFjzfz5882RI0dMly5dTOnSpc3//vc/ExQUZH788UeTO3dus2jRImMMIRv/Z+PGjaZ+/frW0aSFCxea0NBQM3/+fJMyZUpz7tw5e5eIl8SxY8dMgQIFzPjx461tTZs2NSlTprS+3xnzf2EqIiLCHmXCTs6fP29cXFxM9erVrW2xAXrfvn0mTZo0platWubSpUtxHkfIfhihG6+MW7dumRIlSphvv/02TnuvXr2Mq6urCQoKsl5r8EF8EMalS5dMr169zJAhQ+K0T5gwwVgsFuuIN3D8+HFTsGBB07x5c9O1a1djsVjM8ePHrcuPHDlifvzxR5MnTx7z3nvvGYvFYgoXLvzQBxa8Oh53CGdISIg5fvy4ef/9903JkiVNkSJFzE8//WQKFSpkOnfu/NA1cYGEOnDggOnTp49p2bKluX//vrl79651WbNmzUyqVKnMggUL4pwaQ5h6tURHR5vNmzeb7Nmzm1q1asVZdv36dfPaa68Zi8VimjdvbqcKk49Xdwo5vHJiZx2PnVwmIiJCrq6uGjp0qA4dOqRx48YpRYoUatWqldKkSWN9HJPRvNoOHTqkhg0bKioqSl988YWkfyefsVgsat++vYwx6tGjhyIjI9WvXz8mvHrFZc2aVZ9++qk++eQTRURE6Pfff1eePHmsrzcFCxZUwYIFVblyZR0+fFiOjo5avXq1fv/9d9WuXVsxMTG85rxCHvx9z5s3TydOnJCDg4Peeecd5cuXTx4eHpo9e7a2b9+uZcuWqXPnzrp586b8/Pzk7Oxs5+qRnEVERCgwMFBbtmxR4cKF5eTkJCcnJ0VGRsrFxUXTpk2To6OjGjZsqMWLF+utt96SxKSOL7P/vv8YY+Tg4KAKFSpo1qxZatiwoQICArRixQpJkru7uwoXLqzvvvtOhQoVslfZyYbFmEdMkwkkc7Gh6L/ef/99HTx4UEePHpX070zCKVKkUPv27bVjxw5dvnxZU6ZMUd26dfnwC6vWrVvrhx9+UJs2bTRs2DB5eHjE2cdGjBihQYMG6fjx40qfPr2dq4U9PLg/rFixQi1atJCHh4cqVaqkyZMny9HRUVFRUXJycnro9al+/fq6ffu21q5da6/yYQcP7gefffaZ5s6dq1y5csnNzU07d+7UihUrVLp06TiPOXz4sLZt26aWLVs+cl8CnubBfeavv/5Sr169tGnTJvXv31/t2rWTJN27d8/6pU7szNT58uWzW82wvQc/83733Xc6evSoLl26pO7du6tMmTKS/r106vvvv6+MGTPqzTff1KZNm3T//n1t3bpVDg4Oio6O5uo+T0CiwEsnJibG+oYSHh6uW7duWZcNHTpU0dHRev311xUZGWl9gbl+/bq+++47+fv7KzAwUBIj3Pg/33//vT7++GOtWLFCs2fP1u3bt2WxWKyXW+nRo4dOnjxJ4H5FPfiac+7cOfn5+WnXrl0KDAzU3r171bJlS8XExFivT2qxWKyXDpOkVq1aKSQkRNeuXbNL/bCP2H1mwoQJ+umnnzR//nytX79eH3zwgW7cuKEqVapow4YNkqTo6GgZY1S4cGG1adNGTk5OioqKInAj3mLfr8LDwyVJYWFh8vX11bBhw1SmTBnNmTNHM2fOlCQ5OzsrMjJS0r/7J4H75Rf7mffzzz9X//79dePGDTk4OKhq1ar64YcfFBYWpgoVKmjr1q3KlCmTduzYoQwZMmjTpk1ycHBQTEwMgfspSBV4qTz4TV1QUJDeffddFSxYUAMGDNDevXvl6+urqVOn6saNG8qVK5dq164tPz8//f777ypVqpTKlSsnV1fXh66ti1dD7IeSvXv3asqUKZoxY4bWr18vSZo8ebKqVKmi4cOHa86cOQ8F77Rp09qtbtjPg685/fr1U+PGjfX3338re/bsatiwodq0aaODBw+qdevW1sf06NFDmzdvtt7/+eefde3aNQ4XfkU8+P4SFRWlY8eOadCgQSpdurR+/fVXdejQQd98843efPNNvfXWW9q+ffsjP8zGfokDPE3s6Pby5cv1/vvvq2LFimrcuLF+++03+fr6asyYMfLw8NDUqVM1a9YsSZKLi4udq8aLFhwcrFmzZumXX37R9OnT1bFjR929e1edO3fW1KlTFRoaKl9fX61YsUJLly7VwoULlSJFCkVFRTFQFQ/8D+GlEvtH/8UXX2jUqFGqW7euBg0apBkzZmjgwIHasmWLKlasqF27dqlt27by8/PTW2+9pT/++EOSdODAAWXOnFn3798XZ168eiwWixYuXKg33nhD06ZNU79+/fTRRx/ps88+kyRNmzZN5cuX18iRIxUcHGwN3nh1xb7mBAYGasqUKerSpYuyZ88uSUqVKpWaNm2q9u3ba/fu3XrttddUq1YtzZ07V/7+/pL+DV2urq6aO3euPDw87PY88GLEniMpSePGjdPFixfVunVrvf766/rzzz/VvXt3BQUFqWfPnmrQoIHu3LmjChUqaO/evbzW4JlZLBb9+uuvql+/vooVK6Zy5crJ0dFRlStX1uzZs+Xr66tRo0YpTZo0+uabbzRv3jx7l4wXLCIiQuHh4friiy9UokQJLV26VLVr19ZPP/2kbt26KTAwUHPmzNH169clSa6urpL+fU3jC8B4eqHTtgEvwLJly0yePHnM9u3bjTH/Xr7H0dHR5M6d29SqVcts2rTpocdcvnzZdOnSxaRLl84cPnz4RZeMJOKPP/4wXl5eZvz48SYqKsqcO3fOTJw40bi6uprPP//c2q9hw4amZMmS5ubNm/YrFknGzp07ja+vr/W1JSIiwly8eNEsX77cnD9/3hhjzPLly03r1q1NmzZtrJcgjIqKslvNePEenKV8/PjxJkOGDHEuL7dgwQLz+uuvW19X1q1bZ9q2bWtGjRrFZSvxXMLDw02tWrVMr169rG2RkZGmd+/exsnJybofnjp1ynzwwQfm7Nmz9ioVL0jsLPQPzkZ/6NAhc+7cOXPmzBlTpEgRM3LkSGOMMQcPHjQuLi7GYrHEuYwcEoavJpDsPXh4Z3h4uDJlyqQOHTqobNmyWr58uT766CP98MMPyp07t6pVqyZnZ2eFhISobt26kqQLFy5o0aJF2rZtm9atW8cMjK+wv//+W+nSpVOjRo3k6OiobNmyqVmzZoqKitK3336rt956S2XLltW8efN06dKlOLPc49UVGhoqJycnFSxYUDt37tTChQu1dOlSXb58WaVKldLo0aMVEBCggIAA62NiJ1XDqyP2fWrXrl06cOCAJk2aZJ2gSJJCQkK0detWXbt2TcYYjR49Wj4+Puratask9hk8u8jISJ0+fVo1a9aU9H+jk3379tXBgwc1YcIEFS1aVLly5dKMGTPYz15yD35uDgsLU0xMjDw8PFS4cGFJ0pYtW+Tg4KBq1apJ+ndOiU8//VTZs2fX22+/ba+ykz0OL0eyF/vC0bNnT40fP15Zs2bVRx99pNu3b2vEiBHq1auXmjZtqvLlyytfvnzasWOHdu3aZX18lixZ1KBBA61atUrFihWz07NAUpA6dWqdP3/eOru9JLm5ualGjRqKiIjQ5cuXre0+Pj72KBF29qj5HkqUKKErV66oevXqql69ukJCQjRw4ECtW7dO+/fv18mTJ+P0NxyO90qJjo62/rxy5Up99NFH+vXXX63zQMQuf/vtt1WzZk3lzZtXZcuW1alTpzR27FjrY9lnEF/m/58ed/fuXUlSmjRpVLJkSS1fvlwhISGyWCyyWCxydXVVpkyZdO3aNevhwuxnL7cHA/ewYcNUr149+fv7q169evrzzz8VExOj0NBQHT16VKdOndKRI0f0xRdf6OTJk/r444+tkzgi4fjLQrJlHrjsxa5duzRz5kwtWbJEmTJlkiRdvXpVFy9elLe3tyTp5s2bKl68uPr27Wv9pi72xYcA9eqJ3X8OHDggScqfP79y5MihkiVLatasWcqUKZN1xtasWbMqS5Ysunfvnj1Lhp09+GFl27Zt1tl9q1Spoj///FOzZ89WgQIFVKlSJaVKlUoxMTHKnTv3Qx9QODf31RI7CdrBgwetX8zMmDFD8+bNU9myZeXu7i5JSpcunWbNmqV169YpKipKDRs2jHOpOSA+Yt/bVq1apc2bN+vdd99ViRIlVLNmTU2cOFEjRozQJ598otSpU1sfkz59et27d08pUqTg9ekl9+DcR99//70GDhyo4sWLq2bNmmrTpo0WLVqkOnXqqGnTpqpfv758fX2VLl06LV682LoOXo+eDf9rSLZi3xhGjRqlyMhItWvXTuXKlbMuv3v3rlKlSqUtW7bo/v37Wrx4sUJDQ1W/fn1ZLBauJ/gKi/1QsnjxYrVv3149e/ZUpkyZ5O3trdatW2vgwIGKiopSgwYNlC9fPk2cOFEXLlxQ2bJl7V067OTBwN27d2/NmTNHadOm1YkTJxQQEKCvvvpKPXv2lPTvhDTXrl1TkyZNFBUVxeF4r6iFCxdq/fr1Gj9+vLp3764dO3Zo69atGjlypIwx2r59uyZNmqQOHTpYRxnTpk2rBg0aWNcRHR3NB1wkiMVi0aJFi9SsWTP16NFDqVKlkiQ1a9ZMp06d0rJly7R+/XpVrVpVp0+f1pIlS7R9+3aunvAKOXv2rJYvX65p06apVq1aWrt2re7du6fGjRsrQ4YMkv69VGrjxo3l4uKiMmXK8AVgYrDb2eRAIrh9+7apWbOmsVgs5oMPPjDGxJ0UYt68eaZ06dKmcOHC5o033jD37t17qA9eTStWrDApU6Y0kydPNjdu3IizbOHChaZq1arGxcXFFChQwOTIkcP8/vvvdqoU9rRt27Y498eOHWsyZcpkdu3aZYwxZujQocbBwcFs3brVGPPv5Gjjx483ZcqUMeXKlbO+5jBp2qslOjrazJ4921gsFlOmTBmTOnVqc/DgQevyiIgI07p1a/Paa6+Z4cOHm7t371ofBzyPPXv2mEyZMpnp06fHab99+7Yx5t9JHZs1a2bKlStn3n///Tj7JV4NBw4cMDlz5jTGGPPrr7+aVKlSmUmTJhljjAkJCTFTpkx56DG8hz0/izFcFwnJh3ngkPJYf//9t/r06aNFixZpzZo1Klu2bJxv465cuSIHBwelT59eFouFb+qgqKgoNWvWTGnSpNH48eN19+5dnTt3TjNnzlTWrFn1zjvvKEOGDDp8+LAiIyOVLVs262kLeHVUqlRJnp6eWrJkiSwWixwcHNS6dWvlzJlTffr00bx589S2bVsNHjxY7du3V2RkpBwcHHTixAmtXbtWHTt2ZHTgFVe9enWtW7dOH374oWbOnClJun//vlKkSKHIyEh17txZhw8fVq1atfT5558z2ojntmTJEg0dOlQbNmyQxWLRggULNH36dF27dk3lypXT+PHjJf07uZqjoyOvTS+5R31uvnHjhmrWrKny5csrODhYw4cP18cffyxJOnLkiNq0aaMhQ4bo9ddft0fJLy3+0pBsPHh454ULFxQaGqrs2bMra9asGjNmjG7evKnatWtr48aN8vPzs37Q9fLyirMO3mAQO1FIypQptXfvXn3//fc6efKkjh8/Lm9vb23btk0TJkxQkSJF7F0q7GTChAk6c+aMzp8/L0m6dOmSfHx8tG/fPr3xxhvavXu3WrVqpW+++Ubt2rVTVFSUvvnmG5UsWVIBAQEqWLCgJA4PftUFBASoatWq+vrrr9WlSxeNGTPGGrhdXFw0duxYtWjRQmfPnlWKFCnsXS6SodhQde/ePTk7O8sYowsXLujrr7/WmjVr5O3tLV9fX1WvXl3jxo3T22+/rerVq8vFxcXepcPGHjyNMnbCRkdHR6VMmVLFixfX1KlT1bhxY2vgjoiI0Oeff6506dKpQoUKdqv7ZcUnASQLxhhr4O7bt6/Wrl2rw4cP64033lChQoU0aNAgTZ06VW3atFHVqlW1YcMGFSlS5KFv+GLXgVeLeWDStNSpUytXrlxq0KCBevbsqfnz56t69epq1aqV3n//ffXt21e7du1SypQp7V027ChVqlTy9vbWqVOn9MMPPygqKkpDhw5V/fr1FRgYqEuXLun7779XkyZNJP172ZWNGzcqRYoUcS4NxrwRr44HvxiO1aNHD0lSjhw51LJlS0nSmDFjrIHn8OHD+umnn6yvUY8alQIeJ3Z/Wb16tbZv364WLVqofv362rlzpw4fPqxy5cqpRYsWKlasmK5du6ZZs2ZZJ+7Dy+vPP/9U/vz5re8/Q4YM0Z49e/T333+rdevWCggI0JdffqkzZ85oz549ateunXx8fLRhwwbduHFDe/fulYODwyNf0/Ds+J9EshD7IWTQoEGaNGmSvvrqKx05ckSOjo6aOHGi9u/fr4wZM2rixImqVKmSihYtqlOnTvHhBdYPJUuWLFGtWrU0e/ZsXb9+Xc2aNdPGjRu1atUqzZs3T40aNZIk3blzR25ubgoPD7dz5bCn2OuVNmjQQEOHDlXr1q0lSf7+/sqRI4fy58+v0qVLS5IuXryoDz74QHfu3NEnn3xit5phH5999lmcD6mP0qhRIwUHB2vq1Klq166dTp06pTp16ujLL7+UJOtjec9CQsROmtaoUSNFRERY37eGDBmiWbNmafTo0dZLoY4ZM0ZhYWHKkSOH/QqGzX3zzTcqWLCgtm3bJkn66quvNGzYMOXMmVM5c+bUkCFD1LlzZ4WHhys4OFiNGjXSnj17dPDgQRUrVky///67UqRIoaioKAJ3YrPLmeRAAsXExJhr166ZatWqmYULFxpjjFmzZo1JmTKl+f77740xxjph0aVLl8znn3/OpA+wWrZsmXF3dzdTpkwx//zzzyP7HDx40AQGBhoPDw8mlnlFdejQwZw6dcp6v3LlysbZ2dnUqVPHHD582No+e/ZsU7NmTZM6dWpTpEgRU6xYMfPaa68xadoraP/+/aZcuXKmTJky5sCBA8aYx0+GFhUVZZYsWWJSp05t8ufPb0qUKGHdZ4BnsWvXLpM+fXozbdq0OO23bt2y7oczZswwnTp1MunTp2dC0FfAvXv3TIMGDYyXl5fZunWradOmjVm7dq11+ZIlS0z16tXNhx9+aEJCQowxD79m8R5mG0ykhiTrv4e13L59WxUrVtTcuXN1/PhxNW7c2Ho+ZWRkpGbOnKmiRYuqVKlS1scwgRHu3bunpk2bKkuWLBo+fLju3r2rCxcuaM6cOcqdO7dKlSolJycntWrVSlevXtWPP/6ookWL2rtsvGDXr19Xo0aNtHLlSuu5ta1bt1bhwoUVHByswoULq1OnTtbLEp4+fVr79+/XhQsXlD17dr355ptMmvaKWrt2rUaNGqUrV67o+++/l5+f3xMPy/znn3907NgxVaxYUQ4ODuwzeGbz58/XxIkTtXbtWkVERGjp0qWaMWOG7ty5ozJlymjYsGEaO3astmzZogEDBljnmsDL7f79+3rvvfe0du1aeXh46KeffpK/v791+YIFC9S2bVutXLnSesQWbI/QjSRv7dq1Klq0qCwWi6pWraoCBQpo7dq1GjhwoNq3by9JOnHihLp27aqPP/5Y9evXt3PFSEru3r2rN954QyVKlFD37t01cuRIHT16VMePH5enp6dq166tb775Rjt27FDWrFmVNWtWe5eMF+zWrVtKkyaN9VSE4OBgVa5cWTlz5pQkLVu2TJ999pmKFSumTp06PfZ67Q9OWoOXX+ws5NK/4Wfq1KkKCQlRcHCw8ufP/8jgbf5zzjb7DJ7HtGnT1L59ew0cOFALFixQhgwZlDFjRmXIkEGLFy/WwoUL5efnp9u3byt16tT2Lhcv0L1799S5c2d99913mjJlilq1aiXp/07XzJMnj1q1aqXPP//cnmW+UjhYH0lWTEyMDh48qBo1aujYsWPKkCGDvvjiCy1ZskRVqlSxBu7bt2+rW7duioiIUL169excNeztv98jurm5qW3btpo6dapKliypy5cvq2XLlvr7779Vs2ZN7du3T5JUtmxZAvcrqF27dho3bpyuX78ui8WiO3fuqF27dmrcuLEOHz4sY4zq1Kmjb775Rvv379f48eO1e/fuR66L8PTqMMZYA/fgwYM1e/ZsXb58WTt37lTz5s116NChR57j/d9zttlnEF+x723h4eEKDQ2VJDVv3lxdunTRzz//rBIlSqhfv3764Ycf1KtXL7m6uurOnTuSROB+ycXOTP4gZ2dnjRkzRu+995569eql9evXW/ehGzduSJLSp0//Qut81THSjSTvvffe082bNzV//nylSpVKo0aN0qeffqo6deooJiZGYWFh1tkWU6RIwcjBKyx2FGnbtm3at2+fTp8+rQ8++EClSpXS8ePHdenSJfn7+1v3ka5du+qff/7RtGnT5Orqau/yYQetW7fW+vXr1bVrV3344YfKmDGjLl26pDJlyihnzpwaP368ChUqJIvFohUrVujzzz9X1qxZ9e2336pAgQL2Lh92Nm7cOH3++ef6+eeflStXLq1du1azZs1SWFiYfvjhBxUuXJgZgPHcYt/bfv31V40ePVoXL15U9uzZ1bZtW9WrV093796Nc8WNvn37auHChVq3bp18fHzsWDlsKTg4WC1atJD0+KNm7t+/rw8//FCrVq1Ss2bNlCtXLm3YsEFnzpzRvn37OLXlRbLDeeTAI/13IofYCWbmzZtnSpQoYXbu3GldtmHDBtOpUyfTqVMnM3LkSHP//n1jjLH+i1fXwoULTYYMGUydOnXMm2++aVxcXMyXX35pwsPDrX2OHj1qevfuzaRpr7CYmBjrz5988onJkSOHGTlypLl06ZIxxpiLFy8aHx8fU6lSJXPo0CFr/0WLFpmPPvrosZNl4dVx//598+GHH5q2bdvGaf/ll19M0aJFTbly5cyff/5pjIm7vwHPInZC0AEDBpjdu3ebatWqmSxZspgtW7ZY+8yYMcN07NjRpEuXjknTXnKrVq0yFovFdO/e3dr2uAnQ7t27Z5o2bWosFot59913zbhx46yfl5k07cUhdCPJ+e2336wzKsYqWbKkqV+/fpy2/36I4YUDR44cMdmzZzc//PCDMebffcJisZgBAwZY+xw4cMDUq1fP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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    'product_line': ['Health and beauty', 'Electronic accessories', 'Home and lifestyle', 'Food and beverages', 'Fashion accessories', 'Sports and travel'],\n",
    "    'TotalPerProduct': [18560.99, 27102.02, 30036.88, 33170.92, 30437.40, 28574.72]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "df = df.sort_values(by='TotalPerProduct', ascending=False)\n",
    "\n",
    "df['TotalPerProduct'] /= 1000\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "bars = plt.bar(df['product_line'], df['TotalPerProduct'], color='pink')\n",
    "plt.title('Total Sales per Product Line For Females')\n",
    "plt.xlabel('Product Line')\n",
    "plt.ylabel('Total Sales (in thousands)')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "\n",
    "for bar in bars:\n",
    "    height = bar.get_height()\n",
    "    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')\n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "02f27c0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "path_to_csv4 = \"/Users/barbaracastelo/Desktop/PW/ficheiros/Week4/GroupProject/pl_for_male.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "09f1bb93",
   "metadata": {},
   "outputs": [],
   "source": [
    "male_spending = pd.read_csv(path_to_csv4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f022e465",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>product_line</th>\n",
       "      <th>TotalPerProduct</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Home and lifestyle</td>\n",
       "      <td>23825.04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>30632.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Sports and travel</td>\n",
       "      <td>26548.11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Electronic accessories</td>\n",
       "      <td>27235.51</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Food and beverages</td>\n",
       "      <td>22973.93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Fashion accessories</td>\n",
       "      <td>23868.50</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             product_line  TotalPerProduct\n",
       "0      Home and lifestyle         23825.04\n",
       "1       Health and beauty         30632.75\n",
       "2       Sports and travel         26548.11\n",
       "3  Electronic accessories         27235.51\n",
       "4      Food and beverages         22973.93\n",
       "5     Fashion accessories         23868.50"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(male_spending)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "46a87551",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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6aOPPtKdO3c0cuRI9e7dW82bN1eFChWUP39+7dixQ7t27bJunzVrVjVq1Ehr1qxR8eLF7XQULzf+j0Oi8eg1Jj///LMGDRqkEiVKqHbt2mrXrp0WLVqkevXqqXnz5mrYsKFy5sypdOnSafHixdZ98EcGT2P+f9K0NWvW6M8//9R7772nkiVLqnbt2po4caJGjhypzz77TK6urtZt0qdPr/v37ytFihRcW5lERU2CdvDgQeuH2l9++UXz5s1TuXLl5OLiIklKly6dZs2apfXr1ys8PFyNGzeOdpse4FFR7zcHDhyQJBUoUEC5cuVSqVKlNGvWLGXKlMl694Ns2bIpa9asun//vj1Lhp092vmwbds2650yqlatquPHj2v27NkqWLCgKleurNSpUysyMlKvv/56jA4H/lYhinnktmC7du3SzJkztWTJEmXKlEmSdO3aNV2+fFmZM2eWJN26dUslSpRQv379rCNIo85Lvgh8Oj4FIFE5f/68Vq5cqenTp6tOnTpat26d7t+/r2bNmilDhgySHt5apVmzZnJyclLZsmX50Is4s1gsWrRokVq0aKGePXsqderUkqQWLVrozJkzWrFihTZs2KBq1arp7NmzWrJkibZv386Mr0nUwoULtWHDBo0fP149evTQjh07tHXrVo0aNUrGGG3fvl2TJk1Sx44draMd0qZNq0aNGln3ERERwXsPYoj6oLt48WJ16NBBvXr1UqZMmZQ5c2a1bdtWgwYNUnh4uBo1aqT8+fNr4sSJunTpksqVK2fv0mEnjwbuL7/8UnPmzFHatGl16tQp+fj46JtvvlGvXr0kPZxg9vr16/r4448VHh7O5XV4oqjAPXr0aIWFhal9+/YqX768df29e/eUOnVqbdmyRQ8ePNDixYsVFBSkhg0bymKxKCIigtvuxpXdriYH/oMDBw6Y3LlzG2OMWb58uUmdOrWZNGmSMcaYwMBA8+OPP8bYholCEFd79uwxmTJlMjNmzIi2/M6dO8aYhxPRtGjRwpQvX9588MEH5uDBg/YoEy9ARESEmT17trFYLKZs2bLG1dU12u87NDTUtG3b1rzxxhvm+++/N/fu3bNuB8TFqlWrTKpUqczkyZPNzZs3o61buHChqVatmnFycjIFCxY0uXLlMn///bedKoU9bdu2LdrzH374wWTKlMns2rXLGGPMsGHDjIODg9m6dasx5uFnnvHjx5uyZcua8uXLm/v371uXA7G5c+eOqV27trFYLObDDz80xkSfrHjevHmmTJkypkiRIqZ69erWc+rRNng2izHM5Y6Xk3lkyEuUmzdvqnbt2qpQoYKmTZum77//Xp988okk6ciRI2rXrp2GDh2qN9980x4lI5FbsmSJhg0bpo0bN8pisWjBggWaMWOGrl+/rvLly2v8+PGSHk6ulixZMnowXwE1a9bU+vXr1bRpU82cOVOS9ODBA6VIkUJhYWHq0qWLDh8+rDp16qhPnz6MekCchIeHq0WLFkqTJo3Gjx+ve/fuyd/fXzNnzlS2bNn07rvvKkOGDDp8+LDCwsKUPXt263BPvDoqV64sd3d3LVmyRBaLRQ4ODmrbtq1y586tvn37at68efr00081ZMgQdejQQWFhYXJwcNCpU6e0bt06derUidF+iCG2z9cXL15U3759tWjRIq1du1blypWLdt5cvXpVDg4OSp8+vSwWC+fUf8BPCy+lR4erRE1SlCxZMqVKlUolSpTQlClT1KxZM2vgDg0NVZ8+fZQuXTpVrFjRbnUjcYn6w3P//n05OjrKGKNLly7p22+/1dq1a5U5c2blzJlTNWvW1Lhx4/TOO++oZs2acnJysnfpeEF8fHxUrVo1ffvtt+ratavGjh1rDdxOTk764Ycf1KpVK50/f14pUqSwd7lIJKIm/kyVKpX27t2rn3/+WadPn9bJkyeVOXNmbdu2TRMmTFDRokXtXSrsZMKECTp37pwuXLggSbpy5Yo8PT21b98+Va9eXbt371abNm00YsQItW/fXuHh4RoxYoRKlSolHx8fFSpUSBKXuCC6Ry9TuHTpkoKCgpQjRw5ly5ZNY8eO1a1bt1S3bl1t2rRJXl5e1nDt4eERbR+cU/HHTwwvlePHj6tAgQLWwD106FDt2bNHFy9eVNu2beXj46Ovv/5a586d0549e9S+fXt5enpq48aNunnzpvbu3SsHB4dobypAbKIC9x9//KHt27erVatWatiwoXbu3KnDhw+rfPnyatWqlYoXL67r169r1qxZ1gmzkDTF9r7Rs2dPSVKuXLnUunVrSdLYsWOtX7wcPnxYv/32m/V8iq0HATCPTJrm6uqqPHnyqFGjRurVq5fmz5+vmjVrqk2bNvrggw/Ur18/7dq1S6lSpbJ32bCj1KlTK3PmzDpz5oymTp2q8PBwDRs2TA0bNpSvr6+uXLmin3/+WR9//LGkh7dR3bRpk1KkSBHt1mBcb4soxhjr37h+/fpp3bp1Onz4sKpXr67ChQtr8ODBmjJlitq1a6dq1app48aNKlq0aIy/a3y+/m/4qeGlMWLECBUqVEjbtm2TJH3zzTcaPny4cufOrdy5c2vo0KHq0qWLQkJCNG3aNDVp0kR79uzRwYMHVbx4cf39999KkSKFwsPDeUPAM0VNmtakSROFhoYqJCRE0sMvembNmqUxY8ZYb3sxduxYBQcHK1euXPYrGDbzxRdfRPvCLjZNmjTRtGnTNGXKFLVv315nzpxRvXr19PXXX0uSdVsCNx4X9YF1yZIlqlOnjmbPnq0bN26oRYsW2rRpk9asWaN58+apSZMmkqS7d+8qZcqU1vckvJqKFCkiSWrUqJGGDRumtm3bSpK8vb2VK1cuFShQQGXKlJEkXb58WR9++KHu3r2rzz77zG414+UW9fdp8ODBmjRpkr755hsdOXJEyZIl08SJE7V//35lzJhREydOVOXKlVWsWDGdOXOGv2sJxS5XkgOxuH//vmnUqJHx8PAwW7duNe3atTPr1q2zrl+yZImpWbOmadq0qQkMDDTGxJy0iIlCEFe7du0y6dOnN9OnT4+2/Pbt29bz6pdffjGdO3c26dOnZxKjJGr//v2mfPnypmzZsubAgQPGmCdPhhYeHm6WLFliXF1dTYECBUzJkiWtE8oAT7NixQrj4uJifvzxR/Pvv//G2ubgwYPG19fXuLm5MUnjK6pjx47mzJkz1udVqlQxjo6Opl69eubw4cPW5bNnzza1a9c2rq6upmjRoqZ48eLmjTfeYNI0PFVkZKS5fv26qVGjhlm4cKExxpi1a9eaVKlSmZ9//tkYY6zn0JUrV0yfPn04lxIQE6nhpfLgwQO9//77Wrdundzc3PTbb7/J29vbun7BggX69NNPtXr1aus3vMB/MX/+fE2cOFHr1q1TaGioli1bpl9++UV3795V2bJlNXz4cP3www/asmWLBg4caL0+DknPunXrNHr0aF29elU///yzvLy8nnqJyr///qsTJ06oUqVKcnBwYEIZPNX9+/fVvHlzZc2aVd9//73u3bunS5cuac6cOXr99ddVunRpJU+eXG3atNG1a9f066+/qlixYvYuGy/YjRs31KRJE61evdo6P0Tbtm1VpEgRTZs2TUWKFFHnzp2tt3M6e/as9u/fr0uXLilHjhx66623mDQNMTz+t+zOnTuqVKmS5s6dq5MnT6pZs2bWeQHCwsI0c+ZMFStWTKVLl7ZuwzmVMAjdeOncv39fXbp00U8//aQff/xRbdq0kfS/YTF58+ZVmzZt1KdPH3uWiURu+vTp6tChgwYNGqQFCxYoQ4YMypgxozJkyKDFixdr4cKF8vLy0p07d+Tq6mrvcmEDUbOQSw+/hJkyZYoCAwM1bdo0FShQINbgbR67to17lOJZ7t27p+rVq6tkyZLq0aOHRo0apaNHj+rkyZNyd3dX3bp1NWLECO3YsUPZsmVTtmzZ7F0yXrDbt28rTZo01veXadOmqUqVKsqdO7ckacWKFfriiy9UvHhxde7c+Yn3a+f9CE+ybt06FStWTBaLRdWqVVPBggW1bt06DRo0SB06dJAknTp1St26ddMnn3yihg0b2rnipIcLX2FXUTOTP8rR0VFjx47V+++/r969e2vDhg2K+m7o5s2bkqT06dO/0DqRuEWdPyEhIQoKCpIktWzZUl27dtXSpUtVsmRJ9e/fX1OnTlXv3r3l7Oysu3fvShKBO4kyxlgD95AhQzR79mwFBARo586datmypQ4dOhTrNd6PX9vGB1w87vG+jJQpU+rTTz/VlClTVKpUKQUEBKh169a6ePGiateurX379kmSypUrR+B+BbVv317jxo3TjRs3ZLFYdPfuXbVv317NmjXT4cOHZYxRvXr1NGLECO3fv1/jx4/X7t27Y90X70d4XGRkpA4ePKhatWrpxIkTypAhg7766istWbJEVatWtQbuO3fuqHv37goNDVWDBg3sXHXSRE837GLatGlq1aqVpCd/M/vgwQM1bdpUa9asUYsWLZQnTx5t3LhR586d0759+xjqgjiJ6jlYvny5xowZo8uXLytHjhz69NNP1aBBA927dy/aLMH9+vXTwoULtX79enl6etqxcrwI48aNU58+fbR06VLlyZNH69at06xZsxQcHKypU6eqSJEi3A0BcRb1frNt2zbt27dPZ8+e1YcffqjSpUvr5MmTunLliry9va1/97p166Z///1X06dPl7Ozs73Lhx20bdtWGzZsULdu3dS0aVNlzJhRV65cUdmyZZU7d26NHz9ehQsXlsVi0apVq9SnTx9ly5ZN3333nQoWLGjv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\n",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    'product_line': ['Home and lifestyle', 'Health and beauty', 'Sports and travel', 'Electronic accessories', 'Food and beverages', 'Fashion accessories'],\n",
    "    'TotalPerProduct': [23825.04, 30632.75, 26548.11, 27235.51, 22973.93, 23868.50]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "df = df.sort_values(by='TotalPerProduct', ascending=False)\n",
    "\n",
    "df['TotalPerProduct'] /= 1000\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "bars = plt.bar(df['product_line'], df['TotalPerProduct'], color='skyblue')\n",
    "plt.title('Total Sales per Product Line For Males')\n",
    "plt.xlabel('Product Line')\n",
    "plt.ylabel('Total Sales (in thousands)')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "\n",
    "for bar in bars:\n",
    "    height = bar.get_height()\n",
    "    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')\n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e36735ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAxoAAAH8CAYAAABWwtnkAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy88F64QAAAACXBIWXMAAA9hAAAPYQGoP6dpAABCaklEQVR4nO3dd3wc9Z3/8fdsL+rdkjsGjDsG29g002LTLhg4QjiK8eUglKOHhB5wMBgCgR+hBxKSXMIvvwS4UC4UAwlwFNMJNhj3JsmWZNVV2TK/P9YWliXbKqud3Z3X8/HYh7yzq9nP7sOa2fd8m2GapikAAAAASCCH1QUAAAAAyDwEDQAAAAAJR9AAAAAAkHAEDQAAAAAJR9AAAAAAkHAEDQAAAAAJR9AAAAAAkHAEDQAAAAAJR9AAAAAAkHAEDQDYDcMwenV7880397qvRYsW6bnnnhtwPT/96U8HtI9kamxs1J133qkZM2YoLy9PbrdbpaWlmjt3rv7whz+ovb3dkrp++tOfyjAMS14bAOzEZXUBAJCq3n333S73Fy5cqDfeeEOvv/56l+3jxo3b674WLVqk008/XaecckoiS0xZ33zzjebOnastW7boggsu0A033KD8/HxVVlbq5Zdf1oIFC7R8+XItXLjQ6lIBAIOEoAEAu3HIIYd0uV9cXCyHw9Ftux2Fw2EZhiGXq/tpJBKJ6JRTTlFdXZ0++OADHXDAAV0eP+OMM3TzzTfrk08+SVa5gyoUCikQCFhdBgCkHLpOAcAA1NXV6eKLL1ZFRYU8Ho9Gjx6tG264oUu3IMMw1NLSoqeeeqqzu9Xs2bMlSVu3btXFF1+scePGKSsrSyUlJTr66KP11ltv9auetWvXyjAM3XXXXbr99ts1fPhw+Xw+HXzwwVqyZEm353/zzTc666yzVFJSIq/XqwMOOEAPPvhgl+e8+eabMgxDv/vd73T11VeroqJCXq9XK1eu7LGGZ599VsuWLdMNN9zQLWTsMGLEiG6tO42Njbrmmms0atQoeTweVVRU6IorrlBLS0uX5xmGoUsvvVS/+93vdMABBygQCGjy5Ml64YUXur3Oiy++qClTpsjr9WrUqFH6+c9/3mM9pmnqoYce0pQpU+T3+5Wfn6/TTz9dq1ev7vK82bNna8KECfrHP/6hWbNmKRAIaMGCBT3uEwDsjhYNAOintrY2HXXUUVq1apVuvfVWTZo0SW+99ZbuuOMOffrpp3rxxRclxbtgHX300TrqqKN00003SZJycnIkxYOKJN1yyy0qKytTc3Oznn32Wc2ePVtLlizpDCR99ctf/lIjRozQfffdp1gsprvuukvHH3+8/v73v2vmzJmSpGXLlmnWrFkaPny47rnnHpWVlenll1/WZZddppqaGt1yyy1d9nnddddp5syZeuSRR+RwOFRSUtLja7/66quSpH/5l3/pdb2hUEhHHnmkNm7cqOuvv16TJk3Sl19+qZtvvllffPGFXnvttS7jKl588UUtXbpUt912m7KysnTXXXdp3rx5+vrrrzV69GhJ0pIlS/Td735XM2fO1NNPP61oNKq77rpL1dXV3V7/wgsv1G9+8xtddtllWrx4serq6nTbbbdp1qxZ+uyzz1RaWtr53MrKSp199tm69tprtWjRIjkcXLMDgB6ZAIBeOe+888xgMNh5/5FHHjElmX/605+6PG/x4sWmJPOVV17p3BYMBs3zzjtvr68RiUTMcDhsHnPMMea8efO6PCbJvOWWW/b4+2vWrDElmeXl5WZra2vn9sbGRrOgoMA89thjO7fNmTPHHDp0qNnQ0NBlH5deeqnp8/nMuro60zRN84033jAlmUccccRe6zdN05w7d64pyWxra+uyPRaLmeFwuPMWiUQ6H7vjjjtMh8NhLl26tMvv/PnPfzYlmS+99FKXz6G0tNRsbGzs3FZVVWU6HA7zjjvu6Nw2Y8aM3X4OO5/+3n33XVOSec8993R57Q0bNph+v9+89tprO7cdeeSRpiRzyZIlvfosAMDOuAwDAP30+uuvKxgM6vTTT++yff78+ZLUY1elnjzyyCOaOnWqfD6fXC6X3G63lixZouXLl/e7tlNPPVU+n6/zfnZ2tk4++WT94x//UDQaVVtbm5YsWaJ58+YpEAgoEol03k444QS1tbXpvffe67LP0047rd/1SNL9998vt9vdeZs8eXLnYy+88IImTJigKVOmdKllzpw5Pc7sddRRRyk7O7vzfmlpqUpKSrRu3TpJUktLi5YuXbrbz2FnL7zwggzD0Nlnn93ltcvKyjR58uRur52fn6+jjz56QJ8FANgBQQMA+qm2tlZlZWXdpkotKSmRy+VSbW3tXvdx77336qKLLtKMGTP0l7/8Re+9956WLl2quXPnqrW1td+1lZWV9bito6NDzc3Nqq2tVSQS0QMPPNDly7/b7dYJJ5wgSaqpqeny+0OGDOnVaw8fPlySOr/073DWWWdp6dKlWrp0qaZOndrlserqan3++efdasnOzpZpmt1qKSws7Pa6Xq+38zPbtm2bYrHYbj+HXV/bNE2VlpZ2e/333nuv358DANgdYzQAoJ8KCwv1/vvvyzTNLmFjy5YtikQiKioq2us+fv/732v27Nl6+OGHu2xvamoaUG1VVVU9bvN4PMrKypLb7ZbT6dQ555yjSy65pMd9jBo1qsv93q49cdxxx+mxxx7TX//6V11zzTWd20tKSjrHdWRnZ3cZMF9UVCS/368nn3yyx3325rPcWX5+vgzD2O3nsOu+DcPQW2+9Ja/X2+35u25jDQ4A6B2CBgD00zHHHKM//elPeu655zRv3rzO7b/97W87H99h56vtOzMMo9sX2c8//1zvvvuuhg0b1u/annnmGd19992d3Yaampr0/PPP6/DDD5fT6VQgENBRRx2lTz75RJMmTZLH4+n3a+1q3rx5GjdunBYtWqSTTjpJY8eO3evvnHTSSVq0aJEKCwu7BZz+CAaDmj59+m4/h11f+84779SmTZt0xhlnDPi1AQBxBA0A6Kdzzz1XDz74oM477zytXbtWEydO1Ntvv61FixbphBNO0LHHHtv53IkTJ+rNN9/U888/ryFDhig7O1v777+/TjrpJC1cuFC33HKLjjzySH399de67bbbNGrUKEUikX7X5nQ6ddxxx+mqq65SLBbT4sWL1djYqFtvvbXzOffff78OO+wwHX744brooos0cuRINTU1aeXKlXr++ee7LUzYl9d+7rnnNGfOHE2fPl3/8R//odmzZys/P1/19fV6//339dlnn3WZ+vaKK67QX/7yFx1xxBG68sorNWnSJMViMa1fv16vvPKKrr76as2YMaNPdSxcuFBz587Vcccdp6uvvlrRaFSLFy9WMBjsnO1Lkg499FBdcMEFOv/88/Xhhx/qiCOOUDAYVGVlpd5++21NnDhRF110Ub8+CwCwM4IGAPSTz+fTG2+8oRtuuEF33323tm7dqoqKCl1zzTXdpoa9//77dckll+jMM8/snMr1zTff1A033KBQKKQnnnhCd911l8aNG6dHHnlEzz77bLdByH1x6aWXqq2tTZdddpm2bNmi8ePH68UXX9Shhx7a+Zxx48bp448/1sKFC3XjjTdqy5YtysvL07777ts5TqO/9t13X3366ad68MEH9eyzz+pXv/qVQqGQCgoKNHnyZN1+++2dg+aleAvEW2+9pTvvvFOPPfaY1qxZI7/fr+HDh+vYY4/VyJEj+1zDcccdp+eee0433nijvve976msrEwXX3yxWltbuwQuSXr00Ud1yCGH6NFHH9VDDz2kWCym8vJyHXrooZo+ffqAPgsAsCvDNE3T6iIAAImxdu1ajRo1SnfffXeX8REAACQbs04BAAAASDiCBgBkgJEjR+q+++6zugwAADoRNACgj+bPny/DMLrdVq5caXVpGjlypEzTpNsUAMByDAYHgH6YO3eufv3rX3fZVlxcbFE1AACkHlo0AKAfvF6vysrKutycTqeef/55HXTQQfL5fBo9erRuvfXWLtPUGoahRx99VCeddJICgYAOOOAAvfvuu1q5cqVmz56tYDComTNnatWqVZ2/s2rVKn33u99VaWmpsrKyNG3aNL322mt7rK+hoUEXXHCBSkpKlJOTo6OPPlqfffbZoH0eAADsiqABAAny8ssv6+yzz9Zll12mZcuW6dFHH9VvfvMb3X777V2et3DhQp177rn69NNPNXbsWJ111lm68MILdd111+nDDz+UFJ+edofm5madcMIJeu211/TJJ59ozpw5Ovnkk7V+/foe6zBNUyeeeKKqqqr00ksv6aOPPtLUqVN1zDHHdFk/AgCAwcT0tgDQR/Pnz9fvf//7ztWmJen4449XdXW1jj/+eF133XWd23//+9/r2muv1ebNmyXFWzRuvPFGLVy4UJL03nvvaebMmXriiSe0YMECSdLTTz+t888/v8eVxHcYP368Lrroos5AMnLkSF1xxRW64oor9Prrr2vevHnasmVLl1XHx4wZo2uvvVYXXHBB4j4MAAB2gzEaANAPRx11lB5++OHO+8FgUGPGjNHSpUu7tGBEo1G1tbUpFAopEAhIkiZNmtT5eGlpqaT4yuE7b2tra1NjY6NycnLU0tKiW2+9VS+88II2b96sSCSi1tbW3bZofPTRR2publZhYWGX7a2trV26ZAEAMJgIGgDQDzuCxc5isZhuvfVWnXrqqd2ev3Prh9vt7vy3YRi73RaLxSRJP/rRj/Tyyy/r5z//ucaMGSO/36/TTz9dHR0dPdYWi8U0ZMiQHlcWz8vL690b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\n",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data = {\n",
    "    'gender': ['Female', 'Male'],\n",
    "    'TotalPerGender': [167882.92, 155083.82]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.pie(df['TotalPerGender'], labels=df['gender'], autopct='%1.1f%%', colors=['pink', 'lightblue'])\n",
    "plt.title('Total per Gender')\n",
    "plt.axis('equal')  \n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4993e2e1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
