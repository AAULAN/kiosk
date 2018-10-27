import { Component } from '@angular/core';
import { Product } from '../model/product.model';
import { MatDialog } from '@angular/material';
import { ProductDetailsComponent } from './product-details/product-details.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Kiosk';

  constructor (private dialog: MatDialog) {}

  private openProductDialog(product: Product) {
    this.dialog.open(ProductDetailsComponent, {
      height: '315px',
      width: '600px',
      data: { product: product }
    });
  }

  selectProduct(product: Product) {
    this.openProductDialog(JSON.parse(JSON.stringify(product)));
  }

  createProduct() {
    this.openProductDialog(new Product());
  }
}
