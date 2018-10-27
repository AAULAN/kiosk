import { ProductService } from './../../service/product.service';
import { Component, OnInit, Input, Inject } from '@angular/core';
import { Product } from 'src/app/model/product.model';
import { MAT_DIALOG_DATA, MatDialogRef, MatSnackBar } from '@angular/material';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.scss']
})
export class ProductDetailsComponent implements OnInit {
  product: Product;

  constructor(@Inject(MAT_DIALOG_DATA) private data: any,
              private dialogRef: MatDialogRef<ProductDetailsComponent>,
              private productService: ProductService,
              private snackBar: MatSnackBar) { }

  ngOnInit() {
    this.product = this.data.product;
    console.log(this.product);
  }

  submit() {
    let observable: Observable<any>;
    if (this.product.id) {
      observable = this.productService.update(this.product);
    } else {
      observable = this.productService.create(this.product);
    }

    observable.subscribe(data => this.dialogRef.close(true), error => this.snackBar.open(`An error occurred! 🤔 (${error.status})`));
  }
}
