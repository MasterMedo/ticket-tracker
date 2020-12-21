import { useFormik } from 'formik';

export const CreateTicket = () => {
  const formik = useFormik({
    initialValues: {
      title: '',
      content: '',
    },
    onSubmit: values => {
      fetch("/posts/questions", {
        method: "POST",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(values, null, 2)});
    },
  });
  return (
    <form onSubmit={formik.handleSubmit}
      className="border rounded-2 m-2">
      <div style={{float: 'left'}}>
        <label className="" style={{display: 'block'}}
        htmlFor="title">title</label>
        <input className="" style={{display: 'block'}}
          id="title" name="title" type="string"
          onChange={formik.handleChange}
          value={formik.values.title}
        />
      </div>
      <br style={{clear: 'both'}}/>
      <div style={{float: 'left'}}>
        <label className="" style={{display: 'block'}}
          htmlFor="content">content</label>
        <textarea className="ticket-form-content" style={{display: 'block'}}
          id="content" name="content"
          onChange={formik.handleChange}
          value={formik.values.content}
        />
      </div>
      <br style={{clear: 'both'}}/>
      <button type="submit">Submit</button>
    </form>
  );
};
