import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Product } from '../model/product.model';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private api = `${environment.apiBase}/products`;

  constructor(private client: HttpClient) { }

  getAll() {
    return this.client.get<Product[]>(this.api);
  }

  update(product: Product) {
    return this.client.put<any>(`${this.api}/${product.id}`, product);
  }

  create(product: Product) {
    return this.client.post<any>(`${this.api}`, product);
  }
}
