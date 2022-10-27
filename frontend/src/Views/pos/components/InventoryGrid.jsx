import React from 'react'
import { SelectPicker } from 'rsuite';
import api from '../../../common/axiosInterceptors';
import { useQuery } from 'react-query'


const InventoryGrid = () => {
    const { isLoading, data, isError, error } = useQuery('categories-list', () => {

        return api.get("/api/products/")
    })

    let adata = ['Eugenia', 'Bryan', 'Linda', 'Nancy', 'Lloyd', 'Alice', 'Julia', 'Albert'].map(
        item => ({ label: item, value: item })
    );

    return (

        <>
            <SelectPicker data={adata} />
            <SelectPicker data={adata} />
        </>
    )
}

export default InventoryGrid

