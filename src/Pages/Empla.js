import React ,{ useState } from 'react'
//import { useHistory } from 'react-router';
import useFetch from '../components/useFetch';


const Empla = () => {
    const {data:form,isPending,error}= useFetch(' http://127.0.0.1:8000/apis/emploviewset/');
    const [name,setName]=useState('');
    const [address,setAddress]=useState('');
    const [contact,setContact]=useState('');
    const [joining_date,setJoinig_date]=useState('');
 
    
    //const history=useHistory();
    
    const handleSubmit=(e)=>{
        e.preventDefault();
        const form={name,address,contact,joining_date}
        fetch(' http://127.0.0.1:8000/apis/emploviewset/',{
            method:'POST',
            headers:{"Content-Type":"application/json",Authorization:  'Bearer ' + localStorage.getItem('access_token') },
            body:JSON.stringify(form)
        }).then(()=>{
            console.log('New form added')
            console.log(form)
            setName('')
            setJoinig_date('')
            setAddress('')
            setContact('')
            window.location.reload()
        })
    }

    //// DELETE  Item ////
    function deleteitem(id){
      fetch(`http://127.0.0.1:8000/apis/emploviewset/${id}/`,{
        method:'DELETE',
        headers:{ Authorization:  'Bearer ' + localStorage.getItem('access_token'),  },
        }).then(()=>{ window.location.reload() }).catch((err)=>{console.log(err)})
      
    }

    return (
        
    <>
    {error && <div className="content-wrapper">{error}</div>} 
    {isPending&&<div className="content-wrapper">Loading...</div>}
    {form&&
        <div className="content-wrapper">
             <div className="col-lg-12 grid-margin stretch-card">
             <div className="card ">
             < div className="card-body mx-2 my-2">
              <h4 className="card-title">Employees</h4>
               <div className="table-responsive ">
                <table className="table table-hover">
                 <thead>
                   <tr>
                     <th>Name</th>
                     <th>Contact</th>
                     <th>Address</th>
                     <th>Joining Date</th>                    
                   </tr>
                 </thead>
                 <tbody>
               
                 {form.map((form)=>(
                   <tr key={form.id}>
                     <>
                     <td>{form.name}</td>
                     <td>{form.contact}</td>
                     <td>{form.address}</td>
                     <td>{form.joining_date}</td>
                     
                     <td>
                     <button className='btn-sm  btn-inverse-danger ' onClick={()=>(deleteitem(form.id))}>Delete</button>
                     <button className='btn-sm btn-inverse-primary mx-2'>Update</button>
                     </td>
                     </>
                   </tr>
                 ))} 
                 
                 </tbody>
               </table>
               </div>
               </div>
             </div>
             </div>
 



          <div className="col-lg-12 grid-margin stretch-card">
                <div className="card ">
                < div className="card-body mx-2 my-2">

                <div className="card-body">
                <h4 className="card-title">Employees</h4>
                <p className="card-description">
                These are all Employees
                </p>
                <form className="forms-sample" onSubmit={handleSubmit }>
                <div className="form-group">
                    <label htmlFor="exampleInputName1">Name</label>
                    <input type="text" value={name} onChange={(e)=>setName(e.target.value)} className="form-control" autoComplete="off" name='name'  placeholder="Name"/>
                </div>
                <div className="form-group">
                    <label htmlFor="exampleInputName1">Address</label>
                    <input type="text" value={address} onChange={(e)=>setAddress(e.target.value)} className="form-control" autoComplete="off"  name='address'  placeholder="Address"/>
                </div>
                <div className="form-group">
                    <label htmlFor="exampleInputName1">Contact</label>
                    <input type="text" value={contact} onChange={(e)=>setContact(e.target.value)} className="form-control" autoComplete="off"  name='contact'  placeholder="Contact"/>
                </div>
                <div className="form-group">
                    <label htmlFor="exampleInputName1">Date</label>
                    <input type="date" value={joining_date} onChange={(e)=>setJoinig_date(e.target.value)} className="form-control" autoComplete="off"   name='joining_date'  placeholder="Added_on"/>
                </div>
                <button type="submit" className="btn btn-primary me-2">Submit</button>
                <button className="btn btn-light">Cancel</button>
                </form>
                </div>
                </div>
                </div>
         </div>
    </div>
       

    }
    </>
)
}

export default Empla
