import { useFormik } from 'formik';

export const CreateTicket = () => {
  const formik = useFormik({
    initialValues: {
      title: '',
      content: '',
    },
    onSubmit: values => {
      fetch("/tickets/questions", {
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
      className="block border rounded-2 m-2">
      <div>
        <input className="block ticket-form-title"
          id="title" name="title" type="string"
          placeholder="Title"
          onChange={formik.handleChange}
          value={formik.values.title}
        />
      </div>
      <div className="ticket-form-content-parent">
        <textarea className="ticket-form-content"
          id="content" name="content"
          placeholder="content"
          onChange={formik.handleChange}
          value={formik.values.content}
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};
