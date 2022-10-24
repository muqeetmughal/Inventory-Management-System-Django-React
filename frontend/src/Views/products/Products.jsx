import React from 'react'
import { useQuery } from 'react-query';
import { Table } from 'rsuite';
import api from '../../common/axiosInterceptors';

const { Column, HeaderCell, Cell } = Table;




const Products = () => {

    const { isLoading, data, isError, error } = useQuery('list-products', () => {

        return api.get("/api/products/")
    })

    if (isLoading) {
        return <h4>Loading...</h4>
    }
    return (
        <div>
            <Table
                // height={"auto"}
                data={data.data}
                onRowClick={rowData => {
                    console.log(rowData);
                }}s
            >
                <Column width={60} align="center" fixed>
                    <HeaderCell>Id</HeaderCell>
                    <Cell dataKey="id" />
                </Column>

                <Column width={150}>
                    <HeaderCell>Name</HeaderCell>
                    <Cell dataKey="name" />
                </Column>
                <Column width={80} fixed="right">
                    <HeaderCell>...</HeaderCell>

                    <Cell>
                        {rowData => (
                            <span>
                                <a onClick={() => alert(`id:${rowData.id}`)}> Edit </a>
                            </span>
                        )}
                    </Cell>
                </Column>
            </Table>
        </div>
    )
}

export default Products