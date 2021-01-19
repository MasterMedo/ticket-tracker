import { useFormik } from 'formik';
import { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';
import { Category } from '../models/Category';
import { Ticket } from '../models/Ticket';
import { getCategories } from '../actions';

export const CreateTicket = () => {
  const [categories, setCategories] = useState<Category[]>([]);

  let history = useHistory()

  const formik = useFormik({
    initialValues: {
      title: '',
      category_id: 0,
      content: '',
    },
    onSubmit: values => {
      fetch(`/tickets`, {
        method: "POST",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(values, null, 2)
      }).then(r => {
        if (r.ok) {
          return r.json();
        } else {
          throw new Error("couldn't add ticket");
        }
      }).then((ticket: Ticket) => history.push(`/tickets/${ticket.id}`));
    },
  });

  useEffect (() => {
    getCategories().then(data => {
      setCategories(data)
      formik.values.category_id = data[0].id;
    });
  }, []);

  return (
    <form onSubmit={formik.handleSubmit}
      className="block border rounded-2 m-2">
      <select
        name="category_id"
        onChange={formik.handleChange}
        value={formik.values.category_id}
      >
        {categories.map(category =>
          <option key={category.id}
            label={category.name}
            value={category.id}
          />
        )}
      </select>
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
