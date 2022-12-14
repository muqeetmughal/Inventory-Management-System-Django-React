import MainLayout from "./layouts/MainLayout"
import { Routes, Route, Navigate } from 'react-router';
import Users from "./Views/users/Users";
import AddUser from "./Views/users/AddUser";
import Products from "./Views/products/Products";
import Pos from "./Views/pos";
import POSLayout from "./layouts/POSLayout";

const RoutesConfig = () => {


    return (
        <>


            <Routes>
                {/* Public Routes */}

                {/* <Route path='' element={<Navigate to={ENTRY_ROUTE} />} />
                    <Route path="/auth" element={<PublicLayout />}>
                        <Route path="login" element={<Login />} />
                        <Route path="mfa" element={<Mfa />} />
                        <Route path="register" element={<Register />} />
                    </Route> */}


                {/* Protected Routes */}

                <Route path="/" element={<MainLayout />}>
                    {/* <Route path='*' element={<NotFound />} /> */}

                    <Route path="products">
                        <Route path='' element={<Products />} />
                        <Route path='add' element={<AddUser />} />
                    </Route>


                </Route>
                <Route path="/" element={<POSLayout />}>

                    <Route path="pos" element={<Pos />} />
                </Route>

            </Routes>

        </>
    )
}

export default RoutesConfig