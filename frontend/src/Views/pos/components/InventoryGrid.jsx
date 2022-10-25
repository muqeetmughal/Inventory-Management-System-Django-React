import React from 'react'
import { SelectPicker } from 'rsuite';

const data = ['Eugenia', 'Bryan', 'Linda', 'Nancy', 'Lloyd', 'Alice', 'Julia', 'Albert'].map(
    item => ({ label: item, value: item })
);

const InventoryGrid = () => {
    const { isLoading, data, isError, error } = useQuery('categories-list', () => {

        return api.get("/api/products/")
    })

    return (

        <>
            <SelectPicker data={data} />
            <SelectPicker data={data} />
        </>
    )
}

export default InventoryGrid

